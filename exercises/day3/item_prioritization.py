import argparse
import logging
import string
from types import MappingProxyType
from typing import Iterator, List, Set

ALPHABET = list(string.ascii_lowercase) + list(string.ascii_uppercase)
PRIORITIES = MappingProxyType(
    {item: priority for (item, priority) in zip(ALPHABET, range(1, 52 + 1))})


def summed_priorities(filename: str) -> int:
    """
    Compute the sum of priorities of miscategorized items given the rucksack 
    contents in a text file.
    """
    with open(filename, "r") as f:
        file_content = f.read().splitlines()

    miscategorized_items = get_mistakes(file_content)
    priorities = map_items_to_priorities(miscategorized_items)

    return sum(priorities)


def get_mistakes(file_content: List[str]) -> Iterator[str]:
    for rucksack_content in file_content:
        rucksack_content = rucksack_content.strip(" ")

        yield list(get_compartment_overlap(rucksack_content))[0]


def get_compartment_overlap(rucksack_content: str) -> Set[str]:
    n_items = len(rucksack_content)
    assert n_items % 2 == 0, "Uneven amount of items."

    compartment0 = set(rucksack_content[:int(n_items / 2)])
    compartment1 = set(rucksack_content[int(n_items / 2):])

    miscategorized_items = compartment0 & compartment1
    assert len(miscategorized_items) < 2, "More than one miscateorized item."

    return miscategorized_items


def map_items_to_priorities(items: Iterator[str]) -> Iterator[int]:
    for item in items:
        yield PRIORITIES[item]


def run() -> None:
    args = parse_args()
    logging.info(summed_priorities(args.filename))


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
