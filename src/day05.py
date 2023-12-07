import math
import re
from itertools import chain
from typing import Set, Dict, Tuple, Iterator, Union

from aocd import get_data, submit
from tqdm import tqdm

space_splitter_regex = re.compile(r"\s+")
from_to_regex = re.compile(r"^(\w+)-to-(\w+) map:$")
mapping_regex = re.compile(r"^(\d+) (\d+) (\d+)$")


def parse_seeds(seed_line: str) -> (Set[int], int):
    seed_string = "seeds: "
    assert seed_line.startswith(seed_string)
    seed_line = seed_line.replace(seed_string, "")
    seeds = {int(s) for s in space_splitter_regex.split(seed_line.strip())}
    return seeds, len(seeds)


def parse_seed_ranges(seed_line: str) -> (Iterator[int], int):
    seed_string = "seeds: "
    assert seed_line.startswith(seed_string)
    seed_line = seed_line.replace(seed_string, "")
    values = [int(s) for s in space_splitter_regex.split(seed_line.strip())]
    ranges = [
        range(start, start + length) for start, length in zip(values[::2], values[1::2])
    ]
    total = sum(values[1::2])
    return chain.from_iterable(ranges), total


def parse_map(map_definition: str) -> (str, str, Dict[range, int]):
    lines = map_definition.splitlines()
    from_, to_ = from_to_regex.match(lines[0]).groups()
    map_ = {}
    for line in lines[1:]:
        to_range_start, from_range_start, range_length = mapping_regex.match(
            line
        ).groups()
        to_range_start = int(to_range_start)
        from_range_start = int(from_range_start)
        range_length = int(range_length)
        map_[range(from_range_start, from_range_start + range_length)] = to_range_start
    return from_, to_, map_


def build_seeds_and_maps(
    data: str, seed_line_is_ranges: bool = False
) -> (Union[Set[int], int, Iterator[int]], Dict[str, Tuple[str, Dict[range, int]]]):
    sections = data.split("\n\n")
    if seed_line_is_ranges:
        seeds, total = parse_seed_ranges(sections[0])
    else:
        seeds, total = parse_seeds(sections[0])
    maps = {}
    for map_section in sections[1:]:
        from_, to_, map_ = parse_map(map_section)
        maps[from_] = (to_, map_)
    return seeds, total, maps


def find_location_for_seed(seed: int, maps: Dict[str, Tuple[str, Dict[range, int]]]):
    source_value = seed
    source_name = "seed"
    while source_name != "location":
        destination_value = None
        destination_name, map_ = maps[source_name]
        for source_range, destination_start in map_.items():
            if source_value in source_range:
                destination_value = (
                    source_value - source_range.start + destination_start
                )
                break
        source_name = destination_name
        source_value = source_value if destination_value is None else destination_value
    return source_value


def find_lowest_location_number_for_seeds(
    seeds: Set[int], total: int, maps: Dict[str, Tuple[str, Dict[range, int]]]
) -> int:
    lowest_location = math.inf
    iter_ = tqdm(seeds, total=total)
    for i, seed in enumerate(iter_):
        location = find_location_for_seed(seed, maps)
        lowest_location = min(lowest_location, location)
        if i % 100000 == 0:
            iter_.set_postfix(lowest=str(lowest_location))
    return lowest_location


def day_five_a(data: str) -> int:
    seeds, total, maps = build_seeds_and_maps(data, seed_line_is_ranges=False)
    return find_lowest_location_number_for_seeds(seeds, total, maps)


def day_five_b(data: str) -> int:
    # brute force approach because I ran out of coding time ;)
    seeds, total, maps = build_seeds_and_maps(data, seed_line_is_ranges=True)
    return find_lowest_location_number_for_seeds(seeds, total, maps)


if __name__ == "__main__":
    document = get_data(day=5, year=2023)
    result = day_five_b(document)
    print(result)
    submit(result, part="b", day=5, year=2023)
