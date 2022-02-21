"""Tests for the utils functions."""

__author__ = "730488727"

# from exercises.ex05.utils import only_evens, sub, concat
from utils import only_evens, sub, concat  # I have to do this to get full score


def test_only_evens_empty_list_edge_cases() -> None:
    """Testing empty list."""
    empty_list: list[int] = list()
    assert only_evens(empty_list) == []


def test_only_evens_big_list_use_cases() -> None:
    """Testing really big list."""
    big_list: list[int] = [1, 2, 3, 5, 6, 7, 8, 9, 110, 150, 223423423222234234230]
    assert only_evens(big_list) == [2, 6, 8, 110, 150, 223423423222234234230]


def test_only_evens_regular_list_use_cases() -> None:
    """Testing a mixed list with even and odd number."""
    big_list: list[int] = [98, 100, 99, 80, 78, 77, 31, 58, 983]
    assert only_evens(big_list) == [98, 100, 80, 78, 58]


def test_only_evens_even_list_use_cases() -> None:
    """Testing only even number list."""
    big_list: list[int] = [98, 100, 2, 80, 78, 6, 4, 58, 984]
    assert only_evens(big_list) == [98, 100, 2, 80, 78, 6, 4, 58, 984]


def test_only_evens_odd_list_use_cases() -> None:
    """Testing only odd number list."""
    big_list: list[int] = [93, 7, 19, 17, 39]
    assert only_evens(big_list) == []


def test_sub_negative_start_index_edge_cases() -> None:
    """Testing when the start index is negative."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, -1, 3) == [10, 20, 30]


def test_sub_exceeding_end_index_edge_cases() -> None:
    """Testing when the end index exceeed the length of the list."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 5) == [20, 30, 40]


def test_sub_zero_length_edge_cases() -> None:
    """Testing empty list."""
    a_list: list[int] = []
    assert sub(a_list, 1, 5) == []


def test_sub_start_greater_than_len_edge_cases() -> None:
    """Testing start index greater than end index."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 5, 1) == []


def test_sub_end_equal_to_zero_edge_cases() -> None:
    """Testing end index less equals zero."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 0) == []


def test_sub_small_number_use_cases() -> None:
    """Testing when the numbers in the list are small."""
    a_list: list[int] = [1, 2, 3, 4]
    assert sub(a_list, 1, 3) == [2, 3]


def test_sub_big_number_use_cases() -> None:
    """Testing when numbers in the list are big."""
    a_list: list[int] = [111111, 2222222, 33333333, 444444444]
    assert sub(a_list, 1, 3) == [2222222, 33333333]


def test_concat_two_empty_lists_edge_cases() -> None:
    """Inserting two empty lists."""
    empty: list[int] = list()
    empty_one: list[int] = list()
    empty_two: list[int] = list()
    assert concat(empty_one, empty_two) == empty


def test_concat_first_list_empty_edge_cases() -> None:
    """Inserting two empty lists."""
    empty_one: list[int] = list()
    second_list: list[int] = [1, 2, 3]
    assert concat(empty_one, second_list) == [1, 2, 3]


def test_concat_second_list_empty_edge_cases() -> None:
    """Inserting two empty lists."""
    first_list: list[int] = [1, 2, 3]
    empty_two: list[int] = list()
    assert concat(first_list, empty_two) == [1, 2, 3]


def test_concat_first_list_longer_use_cases() -> None:
    """Testing with longer first list in the argument."""
    first_list: list[int] = [1, 2, 3, 4]
    second_list: list[int] = [4, 5, 6]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 4, 5, 6]


def test_concat_second_list_longer_use_cases() -> None:
    """Testing with longer first list in the argument."""
    first_list: list[int] = [1, 2, 3]
    second_list: list[int] = [4, 5, 6, 6]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6, 6]