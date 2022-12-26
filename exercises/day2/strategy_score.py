import argparse
import logging
from typing import Iterator, List


class RPCChoice:

    def __init__(self, value: str) -> None:
        match value:
            case "A" | "X" | "rock":
                self.value = "rock"
                self.score = 1
            case "B" | "Y" | "paper":
                self.value = "paper"
                self.score = 2
            case "C" | "Z" | "scissors":
                self.value = "scissors"
                self.score = 3
            case _:
                raise ValueError(f"Value {value} unknown.")
        
    def __gt__(self, __o) -> bool:
        return (self.score - __o.score) % 3 == 1

    def __eq__(self, __o) -> bool:
        return self.score == __o.score

    def __lt__(self, __o) -> bool:
        return (__o.score - self.score) % 3 == 1


def strategy_score(filename: str) -> int:
    with open(filename, "r") as f:
        file_content = f.read().splitlines()

    scores = _score_per_round(file_content)

    return sum(scores)


def _score_per_round(file_content: List[str]) -> Iterator[int]:
    for line in file_content:
        (opponents_choice_str, own_choice_str) = line.split(" ")
        opponents_choice = RPCChoice(opponents_choice_str)
        own_choice = RPCChoice(own_choice_str)
        choice_score = own_choice.score
        
        yield choice_score + _outcome_score(opponents_choice, own_choice)


def _outcome_score(opponents_choice: RPCChoice, own_choice: RPCChoice) -> int:
        if own_choice > opponents_choice:
            return 6
        elif own_choice < opponents_choice:
            return 0
        else:
            return 3


def run() -> None:
    args = parse_args()
    logging.info(strategy_score(args.filename))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename", "-f", dest="filename", type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()