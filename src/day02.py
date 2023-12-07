import re
from math import prod
from aocd import get_data, submit

space_splitter_regex = re.compile(r"\s+")
game_extractor_regex = re.compile(r"^Game\s+(\d+):\s+")
colors = ["red", "green", "blue"]
color_extractor_regexes = {color: re.compile(rf"(\d+)\s+{color}") for color in colors}
color_max_no = {"red": 12, "green": 13, "blue": 14}


def reduce_line(line: str) -> (int, str):
    game_no = int(game_extractor_regex.match(line).groups()[0])
    reduced_line = game_extractor_regex.sub("", line)
    return game_no, reduced_line


def extract_minimal_number_for_color(color: str, line: str) -> int:
    return max(int(number) for number in color_extractor_regexes[color].findall(line))


def power_of_minimal_set(line: str) -> int:
    minimal_set = [extract_minimal_number_for_color(color, line) for color in colors]
    return prod(minimal_set)


def day_two_a(raw_data: str) -> int:
    sum_ = 0
    for line in raw_data.splitlines():
        game_no, reduced_line = reduce_line(line)
        if all(
            extract_minimal_number_for_color(color, reduced_line) <= color_max_no[color]
            for color in colors
        ):
            sum_ += game_no
    return sum_


def day_two_b(raw_data: str) -> int:
    return sum(power_of_minimal_set(line) for line in raw_data.splitlines())


if __name__ == "__main__":
    document = get_data(day=2, year=2023)
    result = day_two_b(document)
    print(result)
    submit(result, part="b", day=2, year=2023)
