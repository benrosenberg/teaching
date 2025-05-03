import argparse
from interpreter import interpret
from test import run_tests


def main():
    parser = argparse.ArgumentParser(description="Simple Calculator")

    # Optional flags
    parser.add_argument("--test", action="store_true", help="Run the test suite")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    # Positional argument for input file (optional)
    parser.add_argument("file", nargs="?", help="Path to source file to interpret")

    args = parser.parse_args()

    if args.test:
        run_tests(verbose=args.verbose)
    elif args.file:
        try:
            with open(args.file, "r") as f:
                source_code = f.read()
            result = interpret(source_code, verbose=args.verbose)
            if result is not None:
                print(result)
            else:
                print("Interpretation failed (returned None).")
        except FileNotFoundError:
            print(f"File not found: {args.file}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
