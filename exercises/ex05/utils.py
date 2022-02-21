"""Some practice with list functions and unit test."""

__author__ = "730488727"


def only_evens(num_list: list[int]) -> list[int]:
    """Given an list of integers and return a list only with even integers in it."""
    even_num_list: list[int] = list()  # an empty list recording the even numbers
    i: int = 0  # index counter
    while i < len(num_list):
        current_num = num_list[i]
        if (current_num // 2 * 2) == current_num:  # test whether the current number is even
            even_num_list.append(current_num)  # append the number to the list if it is even
        i += 1
    return even_num_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Given an integer list, a starting index, and a ending index. Return an list back starting at the start index(inclusive), and end at the end index(exclusive)."""
    sub_list: list[int] = list()
    if start_index < 0:  # when the starting index is less than zero, set it to zero
        start_index = 0
    if end_index > len(input_list):  # when the ending index is greater than the length of the list, set it to the length of the list
        end_index = len(input_list)
    if (len(input_list) == 0) or (start_index > len(input_list)) or (end_index <= 0):  # when the input list is empty, or the starting index is greater than the length of the list, or the ending index is less than or equal to zero, return an empty list
        return sub_list
    i: int = start_index
    while i < end_index:  # A loop extracting the number out according to the given index
        sub_list.append(input_list[i])
        i += 1
    return sub_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two integer lists, return a list with integers in the first list followed by integers in the second list."""
    final_list: list[int] = list()  # empty list recording the fianl result
    i: int = 0
    while i < len(first_list):  # while loop appending the first list to the final list
        final_list.append(first_list[i])
        i += 1
    i = 0
    while i < len(second_list):  # while loop appending the second list to the final lsit
        final_list.append(second_list[i])
        i += 1
    return final_list