import numpy as np
from aocd import get_data, submit
from scipy.signal import convolve2d


def get_digit_mask(data_array: np.ndarray) -> np.ndarray:
    return np.vectorize(lambda x: x.isdigit())(data_array)


def get_symbol_mask(data_array: np.ndarray) -> np.ndarray:
    return np.vectorize(lambda x: not (x.isdigit() or x == b"."))(data_array)


def grow_symbol_mask(symbol_mask: np.ndarray) -> np.ndarray:
    return convolve2d(
        symbol_mask, np.ones((3, 3), dtype=np.int_), mode="same", boundary="fill"
    ).astype(np.bool_)


def convert_to_numpy_array(data: str) -> np.ndarray:
    width = data.find("\n")
    height = data.count("\n") + 1
    data_as_bytes = data.strip().replace("\n", "").encode("utf-8")
    return np.frombuffer(data_as_bytes, dtype="S1").reshape((height, width))


def find_full_number(
    data_array: np.ndarray, i: int, j_begin: int, grown_symbol_mask: np.ndarray
) -> (int, int):
    j_end = j_begin
    number_counts = grown_symbol_mask[i, j_begin]
    while (
        j_end + 1 < data_array.shape[1] and data_array[i, j_end + 1].decode().isdigit()
    ):
        if grown_symbol_mask[i, j_end + 1]:
            number_counts = True
        j_end += 1
    if number_counts:
        return int("".join(data_array[i, j_begin : j_end + 1].astype(str))), j_end + 1
    else:
        return 0, j_end + 1


def sum_numbers(data_array: np.ndarray, grown_symbol_mask: np.ndarray) -> int:
    sum_ = 0
    i = 0
    while i < data_array.shape[0]:
        j = 0
        while j < data_array.shape[1]:
            if data_array[i, j].decode().isdigit():
                # number begins
                number, j = find_full_number(data_array, i, j, grown_symbol_mask)
                sum_ += number
            else:
                j += 1
        i += 1
    return sum_


def day_three_a(data: str) -> int:
    data_array = convert_to_numpy_array(data)
    symbol_mask = get_symbol_mask(data_array)
    grown_symbol_mask = grow_symbol_mask(symbol_mask)
    return sum_numbers(data_array, grown_symbol_mask)


if __name__ == "__main__":
    document = get_data(day=3, year=2023)
    result = day_three_a(document)
    print(result)
    submit(result, part="a", day=3, year=2023)
