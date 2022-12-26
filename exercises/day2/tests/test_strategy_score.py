import pytest

import strategy_score


class TestRPCChoice():

    @pytest.mark.parametrize("lhs,rhs,expected", [("rock", "rock", False),
                                                  ("rock", "paper", False),
                                                  ("rock", "scissors", True)])
    def test_gt(self, lhs, rhs, expected):
        lhs = strategy_score.RPCChoice(lhs)
        rhs = strategy_score.RPCChoice(rhs)
        assert (lhs > rhs) == expected

    @pytest.mark.parametrize("lhs,rhs,expected", [("rock", "rock", False),
                                                  ("rock", "paper", True),
                                                  ("rock", "scissors", False)])
    def test_lt(self, lhs, rhs, expected):
        lhs = strategy_score.RPCChoice(lhs)
        rhs = strategy_score.RPCChoice(rhs)
        assert (lhs < rhs) == expected

    @pytest.mark.parametrize("lhs,rhs,expected", [("rock", "rock", True),
                                                  ("rock", "paper", False),
                                                  ("rock", "scissors", False)])
    def test_eq(self, lhs, rhs, expected):
        lhs = strategy_score.RPCChoice(lhs)
        rhs = strategy_score.RPCChoice(rhs)
        assert (lhs == rhs) == expected


def test_strategy_score(tmp_path):
    d = tmp_path
    filename = d / "temp.txt"
    with open(filename, "w") as f:
        f.write("A Y\n")
        f.write("B X\n")
        f.write("C Z\n")

    assert strategy_score.strategy_score(filename) == 15
