import pytest

from src.day02 import (
    day_two_a,
    day_two_b,
    reduce_line,
    extract_minimal_number_for_color,
    power_of_minimal_set,
)

example_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
example_expected_a = 8
example_expected_b = 2286


@pytest.mark.parametrize(
    "line, expected",
    (
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            (1, "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            (4, "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"),
        ),
    ),
)
def test_reduce_line(line, expected):
    assert reduce_line(line) == expected


@pytest.mark.parametrize(
    "color, line, expected",
    (
        ("blue", "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 6),
        ("red", "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 4),
        ("green", "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 2),
        ("green", "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green; 15 green", 15),
    ),
)
def test_extract_highest_number_of_color(color, line, expected):
    assert extract_minimal_number_for_color(color, line) == expected


@pytest.mark.parametrize(
    "line, expected",
    (
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            1560,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            630,
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
    ),
)
def test_power_of_minimal_set(line, expected):
    assert power_of_minimal_set(line) == expected


def test_day_two_a():
    assert day_two_a(example_input) == example_expected_a


def test_day_two_b():
    assert day_two_b(example_input) == example_expected_b
