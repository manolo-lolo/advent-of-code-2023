import pytest
import numpy as np

from src.day03a import (
    day_three_a,
    convert_to_numpy_array,
    get_digit_mask,
    get_symbol_mask,
    grow_symbol_mask,
    find_full_number,
    sum_numbers,
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
example_output_a = 4361

test_data_array = np.array(
    [
        [b".", b"#", b"1", b"2", b".", b"."],
        [b"3", b"4", b".", b"+", b"5", b"6"],
    ],
    dtype="|S1",
)


def test_convert_to_numpy_array():
    assert np.array_equal(
        convert_to_numpy_array("..aa..\nbb..aa"),
        np.array(
            [
                [b".", b".", b"a", b"a", b".", b"."],
                [b"b", b"b", b".", b".", b"a", b"a"],
            ],
            dtype="|S1",
        ),
    )


def test_get_digit_mask():
    expected = np.array(
        [
            [False, False, True, True, False, False],
            [True, True, False, False, True, True],
        ],
        dtype=np.bool_,
    )
    assert np.array_equal(get_digit_mask(test_data_array), expected)


def test_get_symbol_mask():
    expected = np.array(
        [
            [False, True, False, False, False, False],
            [False, False, False, True, False, False],
        ],
        dtype=np.bool_,
    )
    assert np.array_equal(get_symbol_mask(test_data_array), expected)


def test_grow_symbol_mask():
    input_symbol_mask = np.array(
        [
            [False, False, False, False, False, False],
            [False, False, False, True, True, False],
            [True, False, False, False, False, False],
        ],
        dtype=np.bool_,
    )

    expected_output = np.array(
        [
            [False, False, True, True, True, True],
            [True, True, True, True, True, True],
            [True, True, True, True, True, True],
        ],
        dtype=np.bool_,
    )
    assert np.array_equal(grow_symbol_mask(input_symbol_mask), expected_output)


example_grown_mask = np.array(
    [
        [False, False, False, True, False, False],
        [True, False, False, False, False, False],
    ],
    dtype=np.bool_,
)


@pytest.mark.parametrize(
    "i_begin, j, expected_number, expected_index",
    ((0, 2, 12, 4), (1, 0, 34, 2), (1, 4, 0, 6)),
)
def test_find_number(i_begin, j, expected_number, expected_index):
    assert find_full_number(test_data_array, i_begin, j, example_grown_mask) == (
        expected_number,
        expected_index,
    )


def test_sum_numbers():
    assert sum_numbers(test_data_array, example_grown_mask) == 12 + 34


def test_day_three_a():
    assert day_three_a(example_input) == example_output_a
