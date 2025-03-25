"""Tests for the Flight class."""

from datetime import datetime

import pytest
from examples.flight import Flight


def test_valid_flight() -> None:
    """Test creating a valid flight."""
    flight = Flight(
        flight_number="BA178",
        departure_airport="JFK",
        arrival_airport="LHR",
        departure_time=datetime(2024, 3, 25, 20, 0),
        arrival_time=datetime(2024, 3, 26, 8, 0),
        departure_timezone="America/New_York",
        arrival_timezone="Europe/London",
    )

    assert flight.flight_number == "BA178"
    assert flight.departure_airport == "JFK"
    assert flight.arrival_airport == "LHR"
    assert flight.duration_minutes is None


def test_invalid_flight_number() -> None:
    """Test invalid flight number format."""
    with pytest.raises(ValueError):
        Flight(
            flight_number="123",  # Invalid format
            departure_airport="JFK",
            arrival_airport="LHR",
            departure_time=datetime(2024, 3, 25, 20, 0),
            arrival_time=datetime(2024, 3, 26, 8, 0),
            departure_timezone="America/New_York",
            arrival_timezone="Europe/London",
        )


def test_invalid_airport_code() -> None:
    """Test invalid airport code length."""
    with pytest.raises(ValueError):
        Flight(
            flight_number="BA178",
            departure_airport="JFKX",  # Too long
            arrival_airport="LHR",
            departure_time=datetime(2024, 3, 25, 20, 0),
            arrival_time=datetime(2024, 3, 26, 8, 0),
            departure_timezone="America/New_York",
            arrival_timezone="Europe/London",
        )


def test_invalid_timezone() -> None:
    """Test invalid timezone."""
    with pytest.raises(ValueError):
        Flight(
            flight_number="BA178",
            departure_airport="JFK",
            arrival_airport="LHR",
            departure_time=datetime(2024, 3, 25, 20, 0),
            arrival_time=datetime(2024, 3, 26, 8, 0),
            departure_timezone="Invalid/Timezone",
            arrival_timezone="Europe/London",
        )


def test_arrival_before_departure() -> None:
    """Test that arrival time must be after departure time."""
    with pytest.raises(ValueError):
        Flight(
            flight_number="BA178",
            departure_airport="JFK",
            arrival_airport="LHR",
            departure_time=datetime(2024, 3, 25, 20, 0),
            arrival_time=datetime(2024, 3, 25, 19, 0),  # Before departure
            departure_timezone="America/New_York",
            arrival_timezone="Europe/London",
        )


def test_duration_calculation() -> None:
    """Test flight duration calculation."""
    flight = Flight(
        flight_number="BA178",
        departure_airport="JFK",
        arrival_airport="LHR",
        departure_time=datetime(2024, 3, 25, 20, 0),
        arrival_time=datetime(2024, 3, 26, 8, 0),
        departure_timezone="America/New_York",
        arrival_timezone="Europe/London",
    )

    duration = flight.calculate_duration()
    assert duration > 0  # Should be positive
    assert duration < 1440  # Should be less than 24 hours


def test_local_times() -> None:
    """Test local time conversion."""
    flight = Flight(
        flight_number="BA178",
        departure_airport="JFK",
        arrival_airport="LHR",
        departure_time=datetime(2024, 3, 25, 20, 0),
        arrival_time=datetime(2024, 3, 26, 8, 0),
        departure_timezone="America/New_York",
        arrival_timezone="Europe/London",
    )

    local_times = flight.to_local_times()
    assert "departure_local" in local_times
    assert "arrival_local" in local_times
    assert local_times["departure_local"].tzinfo is not None
    assert local_times["arrival_local"].tzinfo is not None
