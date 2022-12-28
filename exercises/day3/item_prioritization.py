import argparse
import logging
from typing import Iterator, List


def summed_priorities(filename: str) -> int:
    """Compute the sum of priorities of miscategorized items 
    given the rucksack contents in a text file.
    """
    pass


def run() -> None:
    args = parse_args()
    logging.info(summed_priorities(args.filename))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename", "-f", dest="filename", type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()