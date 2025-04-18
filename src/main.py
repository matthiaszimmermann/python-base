"""Simple Hello World application."""

import sys


def main() -> None:
    """Print a greeting message based on command line arguments."""
    args = sys.argv[1:]

    if not args:
        print("Hello World!")
    else:
        print(f"Hello {args[0]}!")


if __name__ == "__main__":
    main()
