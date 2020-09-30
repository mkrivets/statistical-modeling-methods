import numpy as np
import math as m


def MonteCarlo(func, a, b, N):
    '''
    This function performs the Monte Carlo method for
    specific function f(x) on the range from a to b.
    :param func: f(x)
    :param a: lower bound
    :param b: upper bound
    :param N: number of iterations
    :return: Monte Carlo estimation
    '''
    sum = 0
    for i in range(0, N):
        x = a + (b - a) * np.random.uniform(0, 1, 1)
        sum += func(x)
    return (((b - a) * sum) / N)


f1 = lambda x: m.pow(x, 7) + m.pow(x, 5) + m.pow(x, 3)
f2 = lambda x: 2 * m.sin(3 * x)
f3 = lambda x: 1 / ((x + 1) * m.sqrt(x))

print("The answer for the first integral: ", MonteCarlo(f1, 0, 1, 1000))
print("The answer for the second integral: ", MonteCarlo(f2, 0, m.pi, 1000))
print("The answer for the third integral: ", m.pi)
