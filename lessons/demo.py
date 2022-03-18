def invert(given_dict: dict[str, str]) -> dict[str, str]:
    return_dict: dict[str, str] = {}  # a dictionary to record the inverted key and value
    key_list: list[str] = list()  # a list to record the keys in the new dictionary.
    for i in given_dict:
        for a in key_list:
            if a == given_dict[i]:
                raise KeyError("KeyError")
        return_dict[given_dict[i]] = i
        key_list.append(given_dict[i])
    return return_dict

    {'1': '20', '2': '20'}