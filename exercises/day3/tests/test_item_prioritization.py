import item_prioritization


def test_summed_priorities(tmp_path):
    d = tmp_path
    filename = d / "temp.txt"
    with open(filename, "w") as f:
        f.write("vJrwpWtwJgWrhcsFMMfFFhFp\n")
        f.write("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n")
        f.write("PmmdzqPrVvPwwTWBwg\n")
        f.write("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n")
        f.write("ttgJtRGJQctTZtZT\n")
        f.write("CrZsJsPPZsGzwwsLwLmpwMDw\n")

    assert item_prioritization.summed_priorities(filename) == 157
