import pytest
from src.day04a import points_for_line, day_four_a

input_example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


@pytest.mark.parametrize(
    "test_input, expected",
    (
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
        ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
        ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
        ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
        ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
        (
            "Card 100: 26 67  9 17 82 11 34 47 10 20 | 56 10 73 34 59 62 97 67 12 48 47 20 17 90  7 40 50 13 55  9 27 65 31 38 26",
            128,
        ),
        (
            "Card 175: 83 24 18 84 45 38 23 42 56 14 | 14 76 98 92 46 44 97 20 13 64 72 96 16 68 57 21  6 34  3 19 55 89  9 83  1",
            2,
        ),
    ),
)
def test_parse_line(test_input: str, expected: int) -> None:
    assert points_for_line(test_input) == expected


def test_day_four():
    assert day_four_a(input_example) == 13
