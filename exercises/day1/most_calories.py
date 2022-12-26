def most_calories(filename):

    with open(filename, "r") as f:
        file_content = f.read().splitlines()

    elf_calories = _calories_per_elf(file_content)
    return max(elf_calories)


def _calories_per_elf(file_content):
    elf_calories = 0
    for line in file_content:
        if line != "":
            elf_calories += int(line)
        else:
            yield elf_calories
            elf_calories = 0
