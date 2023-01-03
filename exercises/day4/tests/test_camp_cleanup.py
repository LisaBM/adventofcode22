import camp_cleanup


def test_count_full_overlaps(tmp_path):
    d = tmp_path
    filename = d / "temp.txt"
    with open(filename, "w") as f:
        f.write("2-4,6-8\n")
        f.write("2-3,4-5\n")
        f.write("5-7,7-9\n")
        f.write("2-8,3-7\n")
        f.write("6-6,4-6\n")
        f.write("2-6,4-8\n")

    assert camp_cleanup.count_full_overlaps(filename) == 2
