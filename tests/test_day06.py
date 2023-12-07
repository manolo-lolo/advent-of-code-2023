from src.day06 import (
    day_six_a,
    day_six_b,
    get_times_and_distances,
    get_merged_time_and_distance,
)

example_input = """Time:      7  15   30
Distance:  9  40  200"""
example_expected_a = 288
example_expected_b = 71503


def test_get_times_and_distances():
    assert get_times_and_distances(example_input) == ([7, 15, 30], [9, 40, 200])


def test_get_merged_time_and_distance():
    assert get_merged_time_and_distance(example_input) == (71530, 940200)


def test_day_six_a():
    assert day_six_a(example_input) == example_expected_a


def test_day_six_b():
    assert day_six_b(example_input) == example_expected_b
