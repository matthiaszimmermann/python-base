"""Example of using Pydantic with pytz for flight time handling."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator
import pytz


class Flight(BaseModel):
    """Represents a flight with departure and arrival times in different timezones."""

    flight_number: str = Field(..., pattern=r"^[A-Z]{2}\d{3,4}$")
    departure_airport: str = Field(..., min_length=3, max_length=3)
    arrival_airport: str = Field(..., min_length=3, max_length=3)
    departure_time: datetime
    arrival_time: datetime
    departure_timezone: str = Field(..., pattern=r"^[A-Za-z]+/[A-Za-z_]+$")
    arrival_timezone: str = Field(..., pattern=r"^[A-Za-z]+/[A-Za-z_]+$")
    duration_minutes: Optional[int] = None

    @field_validator("departure_timezone", "arrival_timezone")
    @classmethod
    def validate_timezone(cls, v: str) -> str:
        """Validate that the timezone exists in pytz."""
        try:
            pytz.timezone(v)
        except pytz.exceptions.UnknownTimeZoneError:
            raise ValueError(f"Unknown timezone: {v}")
        return v

    @field_validator("arrival_time")
    @classmethod
    def validate_arrival_time(cls, v: datetime, info) -> datetime:
        """Validate that arrival time is after departure time."""
        departure_time = info.data.get("departure_time")
        if departure_time and v <= departure_time:
            raise ValueError("Arrival time must be after departure time")
        return v

    def calculate_duration(self) -> int:
        """Calculate flight duration in minutes."""
        if self.duration_minutes is not None:
            return self.duration_minutes

        # Convert times to UTC for comparison
        departure_tz = pytz.timezone(self.departure_timezone)
        arrival_tz = pytz.timezone(self.arrival_timezone)

        departure_utc = departure_tz.localize(self.departure_time).astimezone(pytz.UTC)
        arrival_utc = arrival_tz.localize(self.arrival_time).astimezone(pytz.UTC)

        duration = arrival_utc - departure_utc
        return int(duration.total_seconds() / 60)

    def to_local_times(self) -> dict[str, datetime]:
        """Convert times to their respective timezones."""
        departure_tz = pytz.timezone(self.departure_timezone)
        arrival_tz = pytz.timezone(self.arrival_timezone)

        return {
            "departure_local": departure_tz.localize(self.departure_time),
            "arrival_local": arrival_tz.localize(self.arrival_time),
        }


def main() -> None:
    """Example usage of the Flight class."""
    # Example flight from New York to London
    flight = Flight(
        flight_number="BA178",
        departure_airport="JFK",
        arrival_airport="LHR",
        departure_time=datetime(2024, 3, 25, 20, 0),  # 8 PM
        arrival_time=datetime(2024, 3, 26, 8, 0),  # 8 AM next day
        departure_timezone="America/New_York",
        arrival_timezone="Europe/London",
    )

    # Calculate duration
    duration = flight.calculate_duration()
    print(f"Flight duration: {duration} minutes")

    # Get local times
    local_times = flight.to_local_times()
    print(f"Departure (local): {local_times['departure_local']}")
    print(f"Arrival (local): {local_times['arrival_local']}")


if __name__ == "__main__":
    main()
