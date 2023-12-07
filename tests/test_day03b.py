import pytest
import numpy as np

from src.day03b import (
    day_three_b,
    multiply_numbers_around_gear,
    find_fields_around_gear,
    find_full_number_from_middle,
)

example_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
example_output_a = 467835


@pytest.mark.parametrize(
    "gear_i, gear_j, width, height, expected",
    (
        (0, 0, 10, 10, {(0, 1), (1, 0), (1, 1)}),
        (1, 0, 10, 10, {(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)}),
        (9, 9, 10, 10, {(8, 8), (8, 9), (9, 8)}),
        (0, 0, 1, 1, set()),
        (
            4,
            5,
            10,
            10,
            {(3, 4), (3, 5), (3, 6), (4, 4), (4, 6), (5, 4), (5, 5), (5, 6)},
        ),
    ),
    ids=[
        "top_left_boundary",
        "left_boundary",
        "bottom_right_boundary",
        "small_field",
        "middle",
    ],
)
def test_find_fields_around_gear(gear_i, gear_j, width, height, expected):
    assert find_fields_around_gear(gear_i, gear_j, width, height) == expected


@pytest.mark.parametrize(
    "data, i, j_middle, width, expected",
    (
        (["..35..633."], 0, 2, 10, (35, 2, 3)),
        (["..35..633."], 0, 3, 10, (35, 2, 3)),
        (["..35..633."], 0, 6, 10, (633, 6, 8)),
        (["..35..633."], 0, 7, 10, (633, 6, 8)),
        (["..35..633."], 0, 8, 10, (633, 6, 8)),
    ),
)
def test_find_full_number_from_middle(data, i, j_middle, width, expected):
    assert (
        find_full_number_from_middle(
            data,
            i,
            j_middle,
            width,
        )
        == expected
    )


@pytest.mark.parametrize(
    "data, gear_i, gear_j, expected",
    (
        (["467..114..", "...*......", "..35..633."], 1, 3, 467 * 35),
        (["..592.....", "......755.", "...$.*....", ".664.598.."], 2, 5, 755 * 598),
        ([".....114..", "...*......", "..35..633."], 1, 3, 0),
        (["......#...", "617*......", ".....+.58."], 1, 3, 0),
        (["...*......", "..35..633."], 0, 3, 0),
        (["......#...", "...*......", ".....+.58."], 1, 3, 0),
    ),
    ids=[
        "happy_path_1",
        "happy_path_2",
        "only_one_number_1",
        "only_one_number_2",
        "close_to_bound",
        "no_number",
    ],
)
def test_multiply_numbers_around_gear(data, gear_i, gear_j, expected):
    width = len(data[0])
    height = len(data)
    assert multiply_numbers_around_gear(data, gear_i, gear_j, width, height) == expected


def test_day_three_b():
    assert day_three_b(example_input) == example_output_a
