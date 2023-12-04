import re

from aocd import get_data, submit

compiled_re = re.compile(r"\d")


def day_one_a(data: str) -> int:
    final_sum = 0
    for line in data.splitlines():
        matches = compiled_re.findall(line)
        assert len(matches) > 0
        final_sum += int(f"{matches[0]}{matches[-1]}")
    return final_sum


if __name__ == "__main__":
    document = get_data(day=1, year=2023)
    result = day_one_a(document)
    submit(result, part="a", day=1, year=2023)
