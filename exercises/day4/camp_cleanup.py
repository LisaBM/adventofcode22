import argparse
import logging


def count_full_overlaps(filename: str) -> int:
    """
    Compute the sum of priorities of miscategorized items given the rucksack 
    contents in a text file.
    """
    with open(filename, "r") as f:
        file_content = f.read().splitlines()

    return None


def run() -> None:
    args = parse_args()
    logging.info(count_full_overlaps(args.filename))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename",
                        "-f",
                        dest="filename",
                        type=str,
                        required=True)
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()
