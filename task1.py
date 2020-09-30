from scipy import stats

alpha = 0.05
M = 15
m = 27


def pseudorandom(x0, N):
    '''
    This function generates a list of N pseudorandom numbers using a specific
    formula.
    :param x0: first number
    :param N: length of the list
    :return: list
    '''
    result = []
    result.append(x0)
    for i in range(1, N):
        x = (result[i - 1] * (M % pow(2, m))) / (pow(2, m))
        result.append(x)
    return result


print(pseudorandom(1, 100))

stat, p = stats.normaltest(pseudorandom(1, 100))
print("p = {:g}".format(p))

if p < alpha:
    print("The null hypothesis (our pseudorandom numbers come from a normal distribution) can be rejected")
else:
    print("The null hypothesis (our pseudorandom numbers come from a normal distribution) cannot be rejected")
