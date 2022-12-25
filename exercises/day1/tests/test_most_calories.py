import pytest

from most_calories import most_calories


def test_most_calories(tmp_path):
    d = tmp_path
    filename = d / "temp.txt"
    with open(filename, "w") as f:
        f.write("1000\n")
        f.write("2000\n")
        f.write("3000\n")
        f.write("\n")
        f.write("4000\n")
        f.write("\n")
        f.write("5000\n")
        f.write("6000\n")
        f.write("\n")
        f.write("7000\n")
        f.write("8000\n")
        f.write("9000\n")
        f.write("\n")
        f.write("10000")

    assert most_calories(filename) == 24000