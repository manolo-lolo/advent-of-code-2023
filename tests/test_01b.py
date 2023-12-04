from src.day01b import day_one_b, to_int
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet",
            142,
        ),
        (
            """38dbdthfive
onethktvdnfqgfourlxpksevenseven22nine
mjmt18blbfiverjsxjsktkgz
8hlrjjbvsix92grtmthree4
7threetxjztxseven
five5gfgfdjbkrpseven4
8jdzlvrgtcf8eightzpgstwo
bfpqdpfoursevennvgqt8
8one99
kfvmblbtthjrrmktmjmeight4d3lnctfzsvgmjtmd
2eightgppxscjvdgrzjgc3
5twonineknzone
onefourhb4""",
            35 + 19 + 15 + 84 + 77 + 54 + 82 + 48 + 89 + 83 + 23 + 51 + 14,
        ),
        ("athree1o5", 35),
        ("6twones", 61),
        ("eighthree", 83),
        ("oneight", 18),
        ("7", 77),
    ),
    ids=[
        "example_input",
        "long_example",
        "input_with_spelled_out_digit",
        "input_with_overlapping",
        "input_with_overlapping_take_both",
        "input_with_overlapping_take_both2",
        "only_one_digit",
    ],
)
def test_day_one(test_input: str, expected: int):
    assert day_one_b(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected", (("1", 1), ("three", 3)), ids=["digit", "spelled_out_digit"]
)
def test_to_int(test_input: str, expected: int):
    assert to_int(test_input) == expected
