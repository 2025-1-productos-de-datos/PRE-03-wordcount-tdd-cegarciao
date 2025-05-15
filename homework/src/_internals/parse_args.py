import argparse


def parse_args():

    parser = argparse.ArgumentParser(description="count words in files.")

    parser.add_argument(
        "input",
        type=str,
        help="path to the input folder contain files to process",
    )
    parser.add_argument(
        "output",
        type=str,
        help="path to the output for results",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output
