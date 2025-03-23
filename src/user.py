from pydantic import BaseModel, ValidationError

from logging_config import get_logger

logger = get_logger(__name__)


class User(BaseModel):  # noqa: D101
    id: int
    name: str
    email: str

    @classmethod
    def create(cls, user_id: int, name: str, email: str) -> "User":  # noqa: D102
        try:
            return cls(id=user_id, name=name, email=email)
        except ValidationError as e:
            logger.exception(f"Validation error: {e}")  # noqa: G004, TRY401
            raise

    def to_json(self) -> str:  # noqa: D102
        return self.model_dump_json()

    @classmethod
    def from_json(cls, json_str: str) -> "User":  # noqa: D102
        return cls.model_validate_json(json_str)
