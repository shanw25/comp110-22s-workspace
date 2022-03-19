"""Dictionary related utility functions."""

__author__ = "730488727"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:  # loop through each pair of values
        item: str = row[column]  # value of the spedific column
        result.append(item)  # append the value to the list
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]  # get the first row in order to get the name of all columns
    for column in first_row:
        result[column] = column_values(row_table, column)  # append list of all values to the cooresponding name of column
    return result


def head(given_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only first n(2-rd parameter) values."""
    return_dict: dict[str, list[str]] = {}
    for key in given_table:
        current_list: list[str] = []
        if len(given_table[key]) <= num_rows:
            current_list = given_table[key]
        else:
            i: int = 0
            while i < num_rows:  # loop through the value that have smaller index value than the given length
                current_list.append(given_table[key][i])  # append the value of the lsit
                i += 1
        return_dict[key] = current_list  # add the list of the dict
    return return_dict


def select(given_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only selected columns."""
    return_dict: dict[str, list[str]] = {}
    for column in columns:
        return_dict[column] = given_table[column]  # find the selected column and put it in a new dict
    return return_dict


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat two column-based table."""
    return_dict: dict[str, list[str]] = {}
    for key in first_table:  # put everything in the first table to a new dict
        return_dict[key] = first_table[key]
    for key in second_table:
        if key in return_dict:  # if the current key is in the return_table
            return_dict[key] += second_table[key]  # add the list to that dict according to its value
        else:
            return_dict[key] = second_table[key]  # if not in the return_table, initialize a new column
    return return_dict


def count(keys: list[str]) -> dict[str, int]:
    """Count the number of times each value appeared in the given list."""
    return_dict: dict[str, int] = {}
    for key in keys:
        if key in return_dict:  # if exists in the current list, add 1 to the index value
            return_dict[key] += 1
        else:
            return_dict[key] = 1  # if not, initialze a new dict pair and set the value to 1
    return return_dict