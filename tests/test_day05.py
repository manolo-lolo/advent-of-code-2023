from src.day05 import day_five_a, day_five_b, parse_seeds, parse_seed_ranges, parse_map

example_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
example_expected_a = 35
example_expected_b = 46


def test_parse_seeds():
    assert parse_seeds("seeds: 79 14 55 13") == ({79, 14, 55, 13}, 4)


def test_parse_seed_ranges():
    iter_, total = parse_seed_ranges("seeds: 79 14 55 13")
    assert total == 27
    assert set(iter_) == set(list(range(79, 79 + 14)) + list(range(55, 55 + 13)))


def test_parse_map():
    actual_from, actual_to, actual_map = parse_map(
        """soil-to-fertilizer map:
0 15 0
37 52 1
39 0 2"""
    )
    assert actual_from == "soil"
    assert actual_to == "fertilizer"
    assert actual_map == {range(15, 15): 0, range(52, 53): 37, range(0, 2): 39}


def test_day_five_a():
    assert day_five_a(example_input) == example_expected_a


def test_day_five_b():
    assert day_five_b(example_input) == example_expected_b
