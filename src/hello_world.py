import sys


def main() -> None:
    """Print 'hello world' to the console."""
    if len(sys.argv) >= 2:
        print(f"hello {sys.argv[1]}!")
    else:
        print("hello world!")


if __name__ == "__main__":
    main()
