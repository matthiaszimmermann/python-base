import json
import sys

from user import User


def print_usage(app: str) -> None:  # noqa: D103
    print(f"Usage: python {app} <json_string>")  # noqa: T201
    print(f"   or: python {app} <id> <name> <email>")  # noqa: T201


def json_to_args(json_str: str) -> tuple[int, str, str]:  # noqa: D103
    try:
        user = User.from_json(json_str)
        return (user.id, user.name, user.email)  # noqa: TRY300
    except json.JSONDecodeError as ed:
        print(f"Invalid JSON string provided: {ed}")  # noqa: T201
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"Error creating user from JSON: {e}")  # noqa: T201
        sys.exit(2)


def args_to_json(argv: list) -> str:  # noqa: D103
    # id, name, email provided
    try:
        user_id = int(argv[0])
        name = argv[1]
        email = argv[2]
        user = User.create(user_id, name, email)
        return user.to_json()
    except ValueError as ve:
        print(ve)  # noqa: T201
        sys.exit(3)
    except Exception as e:  # noqa: BLE001
        print(e)  # noqa: T201
        sys.exit(4)


def main() -> None:  # noqa: D103
    if len(sys.argv) == 2:  # noqa: PLR2004
        (user_id, name, email) = json_to_args(sys.argv[1])
        print(f"{user_id} {name} {email}")  # noqa: T201
    elif len(sys.argv) == 4:  # noqa: PLR2004
        user_json = args_to_json(sys.argv[1:])
        print(user_json)  # noqa: T201
    else:
        print_usage(sys.argv[0])


if __name__ == "__main__":
    main()
