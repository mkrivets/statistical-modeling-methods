M = 567
m = 11234


def pseudorandom(x0, N):
    '''
    This function generates a list of N pseudorandom numbers using a specific
    formula.
    :param x0: first number
    :param N: length of the list
    :return:
    '''
    result = []
    result.append(x0)
    for i in range(1, N):
        x = (result[i - 1] * (M % pow(2, m))) / pow(2, m)
        result.append(x)
    return result


print(pseudorandom(1, 100))
