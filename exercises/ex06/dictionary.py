"""Practice with dictionary: ex06."""

__author__ = "730488727"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Invert every key and value in the given dictionary. If value is repeated, KeyError will be raised."""
    return_dict: dict[str, str] = {}  # a dictionary to record the inverted key and value
    key_list: list[str] = list()  # a list to record the keys in the new dictionary.
    is_contain: bool = False  # boolean tracking whether the current key value is repeated in the inverted dictionary
    for i in given_dict:
        for index in key_list:  # check whether the current key value is repeated
            if index == given_dict[i]:
                is_contain = True
        if is_contain:
            raise KeyError("KeyError")  # raise KeyError when repeated
        return_dict[given_dict[i]] = i  # add the pair to the final dictionary
        key_list.append(given_dict[i])  # append the current key to the tracking list
    return return_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """Show student's favorite color recorded in a dictionary."""
    times_mentioned_tracking_dict: dict[str, int] = dict()  # key: color mentioned, value: times mentioned
    for i in given_dict:  # add the color to the key of the dictionary if mentioned and count the times that each color is mentioned
        if given_dict[i] in times_mentioned_tracking_dict:  # if the color already exist in the dict, add 1 to the value
            times_mentioned_tracking_dict[given_dict[i]] += 1
        else:  # if the color doesn't exist in the dict, set the value to 1
            times_mentioned_tracking_dict[given_dict[i]] = 1
    favo_color: str = ""  # record the favorite color
    current_times_mentioned: int = 0  # record the times that the current color is mentioned
    for i in times_mentioned_tracking_dict:  # scan through the list to find the color that mentioned for the most of the time.
        if times_mentioned_tracking_dict[i] > current_times_mentioned:  # if the current color has similar mentioned times as the previous color, the previous color will be recorded
            favo_color = i
            current_times_mentioned = times_mentioned_tracking_dict[i]
    return favo_color


def count(given_list: list[str]) -> dict[str, int]:
    """Count the number of times each string in the list appeared."""
    times_mentioned_tracking_dict: dict[str, int] = dict()  # key: string in the given_list, value: times mentioned
    for i in given_list:  # loop through each string in the given list
        if i in times_mentioned_tracking_dict:  # if the string already exist in the dict, add 1 to the value
            times_mentioned_tracking_dict[i] += 1
        else:  # if the string doesn't exist in the dict, set the value to 1
            times_mentioned_tracking_dict[i] = 1
    return times_mentioned_tracking_dict