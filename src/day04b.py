import re

from aocd import get_data, submit

card_no_regex = re.compile(r"Card\s+\d+:")
space_splitter_regex = re.compile(r"\s+")


def number_of_winning_numbers_for_line(line: str) -> int:
    line = card_no_regex.sub("", line)
    first_half, second_half = line.split("|")
    winning_numbers = set(space_splitter_regex.split(first_half.strip()))
    picked_numbers = set(space_splitter_regex.split(second_half.strip()))
    # ensure there are no duplicated numbers
    assert len(winning_numbers) == len(space_splitter_regex.split(first_half.strip()))
    assert len(picked_numbers) == len(space_splitter_regex.split(second_half.strip()))

    picked_winning_numbers = winning_numbers.intersection(picked_numbers)
    return len(picked_winning_numbers)


def day_four_b(data: str) -> int:
    data = data.strip()
    number_of_cards = {i: 1 for i in range(data.count("\n") + 1)}
    for i, line in enumerate(data.splitlines()):
        number_of_winning_numbers = number_of_winning_numbers_for_line(line)
        for j in range(i + 1, i + 1 + number_of_winning_numbers):
            number_of_cards[j] += number_of_cards[i]
    return sum(number_of_cards.values())


if __name__ == "__main__":
    document = get_data(day=4, year=2023)
    result = day_four_b(document)
    submit(result, part="b", day=4, year=2023)
