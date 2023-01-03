import argparse
import logging
from typing import Iterator, List, Tuple


def count_full_overlaps(filename: str) -> int:
    """
    Count the number of full section overlaps given the paired section
    assignments in a text file.
    """
    with open(filename, "r") as f:
        file_content = f.read().splitlines()

    section_pairs = format_lines_to_sections(file_content)

    return sum([is_full_overlap(p) for p in section_pairs])


def format_lines_to_sections(lines: List[str]) -> Iterator[Tuple[set, set]]:
    for line in lines:
        first, second = line.split(",")

        yield section_str_to_set(first), section_str_to_set(second)


def section_str_to_set(section_str: str) -> set:
    """Convert section spec as range to a set containing all sections."""
    start, end = section_str.split("-")
    return set(range(int(start), int(end) + 1))


def is_full_overlap(pair: Tuple[set, set]) -> bool:
    return pair[0].issubset(pair[1]) | pair[1].issubset(pair[0])


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
