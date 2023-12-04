from src.day01a import day_one_a
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet",
            142,
        ),
        ("athree1o5", 15),
        ("6twones", 66),
        ("7", 77),
    ),
    ids=[
        "example_input",
        "input_with_spelled_out_digit",
        "input_with_overlapping",
        "only_one_digit",
    ],
)
def test_day_one(test_input: str, expected: int):
    assert day_one_a(test_input) == expected
