import argparse
import logging
from typing import Iterator, List


def most_calories(filename: str) -> int:
    """Return the sum of calories the elf with the most calories carries."""

    with open(filename, "r") as f:
        file_content = f.read().splitlines()

    elf_calories = _calories_per_elf(file_content)
    return max(elf_calories)


def _calories_per_elf(file_content: List[str]) -> Iterator[int]:
    elf_calories = 0
    for line in file_content:
        if line != "":
            elf_calories += int(line)
        else:
            yield elf_calories
            elf_calories = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename",
                        "-f",
                        dest="filename",
                        type=str,
                        required=True)
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    logging.info(most_calories(args.filename))


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()
