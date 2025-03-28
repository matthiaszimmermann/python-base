import sys


def main() -> None:
    """Print 'hello world' to the console."""
    if len(sys.argv) == 1:
        print("hello world!")
    else:
        print(f"hello {sys.argv[1]}!")


if __name__ == "__main__":
    main()
