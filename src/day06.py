import math
import re
from itertools import chain
from typing import Set, Dict, Tuple, Iterator, Union, List

from aocd import get_data, submit
from tqdm import tqdm
from math import sqrt, ceil, floor

space_splitter_regex = re.compile(r"\s+")
from_to_regex = re.compile(r"^(\w+)-to-(\w+) map:$")
mapping_regex = re.compile(r"^(\d+) (\d+) (\d+)$")


def get_times_and_distances(raw_data: str) -> (List[int], List[int]):
    assert raw_data.count("\n") == 1
    time_line, distance_line = raw_data.splitlines()
    time_line = re.sub(r"Time:\s*", "", time_line)
    distance_line = re.sub(r"Distance:\s*", "", distance_line)
    times = [int(s) for s in space_splitter_regex.split(time_line)]
    distances = [int(s) for s in space_splitter_regex.split(distance_line)]
    return times, distances


def get_merged_time_and_distance(raw_data: str) -> (int, int):
    assert raw_data.count("\n") == 1
    time_line, distance_line = raw_data.splitlines()
    time_line = re.sub(r"Time:\s*", "", time_line)
    time_line = space_splitter_regex.sub("", time_line)
    distance_line = re.sub(r"Distance:\s*", "", distance_line)
    distance_line = space_splitter_regex.sub("", distance_line)
    return int(time_line), int(distance_line)


def get_possible_distances(max_time: int) -> List[int]:
    return [time_press * (max_time - time_press) for time_press in range(1, max_time)]


def day_six_a(raw_data: str) -> int:
    multiplication = 1
    times, distances = get_times_and_distances(raw_data)
    for time, distance_record in zip(times, distances):
        possible_distances = get_possible_distances(time)
        number_of_ways = sum(
            1
            for possible_distance in possible_distances
            if possible_distance > distance_record
        )
        multiplication *= number_of_ways
    return multiplication


def day_six_b(raw_data: str) -> int:
    max_time, distance_record = get_merged_time_and_distance(raw_data)
    # max_time = 62737565
    # distance_record = 644102312401023

    # x * (max_time - x) > distance_record
    # x ** 2 - x * max_time + distance_record == 0
    x1 = max_time / 2 - sqrt(max_time**2 / 4 - distance_record)
    x2 = max_time / 2 + sqrt(max_time**2 / 4 - distance_record)
    lower_included_boundary = ceil(x1 + 1e-9)
    higher_included_boundary = floor(x2 - 1e-9)
    number_of_ways = range(lower_included_boundary, higher_included_boundary + 1)
    return len(number_of_ways)


if __name__ == "__main__":
    document = get_data(day=6, year=2023)
    result = day_six_b(document)
    print(result)
    submit(result, part="b", day=6, year=2023)
