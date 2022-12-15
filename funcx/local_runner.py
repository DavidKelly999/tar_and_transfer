import argparse
from tar import create_tar


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(create_tar(args.inputs, args.output))


if __name__ == "__main__":
    main()
