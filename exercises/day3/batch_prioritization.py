import argparse
import logging
from typing import Iterator, List

import item_prioritization


def summed_batch_priorities(filename: str) -> int:
    """
    Compute the sum of priorities of batches given the rucksack contents in a 
    text file.
    """
    with open(filename, "r") as f:
        file_content = f.read().splitlines()

    group_items = group_input(file_content, group_size=3)
    batch_symbols = get_batch_symbol(group_items)
    batch_priorities = item_prioritization.map_items_to_priorities(
        batch_symbols)
    return sum(batch_priorities)


def group_input(file_content: List[str], group_size: int) -> zip:
    """Group rucksack contents into groups of size group_size."""
    return zip(*(iter(file_content),) * group_size)


def get_batch_symbol(grouped_items: zip) -> Iterator[str]:
    """Extract batch symbol from each group of rucksack contents."""
    for group in grouped_items:
        batch_symbol = set.intersection(*[set(g) for g in group])
        assert len(batch_symbol) == 1, "More than one item shared in group."

        yield list(batch_symbol)[0]


def run() -> None:
    args = parse_args()
    logging.info(summed_batch_priorities(args.filename))


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
