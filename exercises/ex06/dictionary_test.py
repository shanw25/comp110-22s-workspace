"""Unit test for ex06: dictionaory."""

__author__ = "730488727"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_short_dict_use_case() -> None:
    """Test a really short dictionary: use case."""
    potential_dict1: dict[str, str] = {"a": "aa"}
    assert invert(potential_dict1) == {"aa": "a"}


def test_invert_long_dict_use_case() -> None:
    """Test a long dictionary: use case."""
    potential_dict2: dict[str, str] = {"a": "aa", "b": "bb", "c": "cc", "d": "dd", "e": "ee"}
    assert invert(potential_dict2) == {"aa": "a", "bb": "b", "cc": "c", "dd": "d", "ee": "e"}


def test_invert_value_repeat_edge_case() -> None:
    """Test a repeated value dictionary: edge case."""
    with pytest.raises(KeyError):
        potential_dict3: dict[str, str] = {"a": "aa", "b": "aa"}
        invert(potential_dict3)


def test_favorite_color_big_dict_use_case() -> None:
    """Test a small dict: use case."""
    favo_color: dict[str, str] = {"A": "yellow", "B": "green", "C": "black", "D": "blue", "E": "blue"}
    assert favorite_color(favo_color) == "blue"


def test_favorite_color_small_dict_use_case() -> None:
    """Test a small dict: use case."""
    favo_color: dict[str, str] = {"C": "green", "A": "yellow", "B": "yellow"}
    assert favorite_color(favo_color) == "yellow"


def test_favorite_color_no_repeat_edge_case() -> None:
    """Test for a dict that none of the favorite color repeats."""
    favo_color: dict[str, str] = {"A": "yellow", "B": "green", "C": "black", "D": "blue", "E": "purple", "F": "white"}
    assert favorite_color(favo_color) == "yellow"


def test_count_small_list_use_case() -> None:
    """Test counting a small list."""
    str_list: list[str] = ["apple"]
    assert count(str_list) == {"apple": 1}


def test_count_large_list_use_case() -> None:
    """Test counting a large list."""
    str_list: list[str] = ["apple", "banana", "apple", "banana", "pear", "python", "java", "pear", "java"]
    assert count(str_list) == {"apple": 2, "banana": 2, "pear": 2, "python": 1, "java": 2}


def test_count_empty_list_edge_case() -> None:
    """Test counting an empty list."""
    str_list: list[str] = []
    assert count(str_list) == {}


def test_count_repeat_one_string_list() -> None:
    """Test counting an list only repeating one string."""
    str_list: list[str] = ["a", "a", "a", "a", "a"]
    assert count(str_list) == {"a": 5}