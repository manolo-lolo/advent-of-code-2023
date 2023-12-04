import re

from aocd import get_data, submit

spelled_out_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
compiled_re = re.compile(r"(?=(\d|" + "|".join(spelled_out_to_int.keys()) + "))")


def to_int(inp: str) -> int:
    if inp in spelled_out_to_int:
        return spelled_out_to_int[inp]
    else:
        return int(inp)


def day_one_b(data: str) -> int:
    final_sum = 0
    for line in data.splitlines():
        matches = compiled_re.findall(line)
        assert len(matches) > 0
        final_sum += int(f"{to_int(matches[0])}{to_int(matches[-1])}")
    return final_sum


if __name__ == "__main__":
    document = get_data(day=1, year=2023)
    result = day_one_b(document)
    submit(result, part="b", day=1, year=2023)
