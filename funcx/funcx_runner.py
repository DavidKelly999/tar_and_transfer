import argparse
from funcx import FuncXExecutor


def main(args):
    with FuncXExecutor(endpoint_id=args.endpoint_id) as fxe:
        future = fxe.submit(args.function_id, args.inputs, args.output)
        print(future.result())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", "--input", nargs="+", required=True, help="File(s) to tar")
    parser.add_argument("--output", required=True, help="Tar filename")
    parser.add_argument("--function_id", required=True, help="Funcx function id")
    parser.add_argument("--endpoint_id", required=True, help="Funcx endpoint id")
    parser_args = parser.parse_args()
    main(parser_args)
