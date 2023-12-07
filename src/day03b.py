from typing import List, Set, Tuple

from aocd import get_data, submit


def find_fields_around_gear(
    gear_i: int, gear_j: int, width: int, height: int
) -> Set[Tuple[int, int]]:
    return {
        (i, j)
        for i in range(gear_i - 1, gear_i + 2)
        for j in range(gear_j - 1, gear_j + 2)
        if 0 <= i < height and 0 <= j < width and (i != gear_i or j != gear_j)
    }


def find_full_number_from_middle(
    data: List[str],
    i: int,
    j_middle: int,
    width: int,
) -> (int, int, int):
    j_end = j_middle
    while j_end + 1 < width and data[i][j_end + 1].isdigit():
        j_end += 1
    j_begin = j_middle
    while j_begin - 1 >= 0 and data[i][j_begin - 1].isdigit():
        j_begin -= 1

    return (
        int(data[i][j_begin : j_end + 1]),
        j_begin,
        j_end,
    )


def multiply_numbers_around_gear(
    data: List[str], gear_i: int, gear_j: int, width: int, height: int
) -> int:
    scan_fields = find_fields_around_gear(gear_i, gear_j, width, height)
    numbers = []
    while len(numbers) < 2 and len(scan_fields) > 0:
        i, j = scan_fields.pop()
        if data[i][j].isdigit():
            number, j_begin, j_end = find_full_number_from_middle(data, i, j, width)
            numbers.append(number)
            for j_remove in range(j_begin, j_end + 1):
                scan_fields.discard((i, j_remove))

    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0


def day_three_b(raw_data: str) -> int:
    data = raw_data.splitlines()
    width = raw_data.find("\n")
    height = raw_data.count("\n") + 1
    sum_ = 0
    for i in range(height):
        for j in range(width):
            if data[i][j] == "*":
                product_ = multiply_numbers_around_gear(data, i, j, width, height)
                sum_ += product_
    return sum_


if __name__ == "__main__":
    document = get_data(day=3, year=2023)
    result = day_three_b(document)
    print(result)
    submit(result, part="b", day=3, year=2023)
