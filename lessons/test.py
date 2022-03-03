def luhn(number: int) -> bool:
    str_number: str = str(number)
    result_number: list[int] = []
    i: int = len(str_number) - 2
    su: int = 0
    result_number.append(int(str_number[i + 1]))
    while i >= 0:
        result_number.append(int(str_number[i]) * 2)
        if (i - 1) >= 0:
            result_number.append(int(str_number[i - 1]))
        i -= 2
    ind: int = 0
    for index in result_number:
        if len(str(index)) != 1:
            result_number[ind] = result_number[ind] - 9
            su += result_number[ind]
            ind += 1
        else:
            su += result_number[ind]
            ind += 1
    # 这样就把它们同时也都加起来了，sum是在su这个变量里面
    if su % 10 == 0:
        return True
    return False
