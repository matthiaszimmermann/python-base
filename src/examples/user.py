"""Example of using Pydantic for user data validation."""

from pydantic import BaseModel, EmailStr, Field

from logging_config import get_logger

logger = get_logger(__name__)


class User(BaseModel):
    """Represents a user with basic profile information."""

    id: int
    name: str = Field(..., min_length=2)  # Added min_length validation to match test
    email: EmailStr  # Using EmailStr for email validation

    def to_json(self) -> str:  # noqa: D102
        return self.model_dump_json()

    @classmethod
    def from_json(cls, json_str: str) -> "User":  # noqa: D102
        return cls.model_validate_json(json_str)


def main() -> None:
    """Show how to use the User class."""
    user = User(id=1, name="Alice Smith", email="alice.smith@example.com")

    print(f"User: {user.name}")
    print(f"Email: {user.email}")
    print(f"ID: {user.id}")


if __name__ == "__main__":
    main()
