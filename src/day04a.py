import re

from aocd import get_data, submit

card_no_regex = re.compile(r"Card\s+\d+:")
space_splitter_regex = re.compile(r"\s+")


def points_for_line(line: str) -> int:
    line = card_no_regex.sub("", line)
    first_half, second_half = line.split("|")
    winning_numbers = set(space_splitter_regex.split(first_half.strip()))
    picked_numbers = set(space_splitter_regex.split(second_half.strip()))
    # ensure there are no duplicated numbers
    assert len(winning_numbers) == len(space_splitter_regex.split(first_half.strip()))
    assert len(picked_numbers) == len(space_splitter_regex.split(second_half.strip()))

    picked_winning_numbers = winning_numbers.intersection(picked_numbers)
    if len(picked_winning_numbers) == 0:
        return 0
    else:
        return 2 ** (len(picked_winning_numbers) - 1)


def day_four_a(data: str) -> int:
    return sum(points_for_line(line) for line in data.splitlines())


if __name__ == "__main__":
    document = get_data(day=4, year=2023)
    result = day_four_a(document)
    submit(result, part="a", day=4, year=2023)
