import numpy as np
from scipy import stats
import math as m


def normalDistributionModeling1(N):
    '''
    This function returns a list of N implementations of the random variable which is based
    on the other random variable, for example, uniformly distributed on the (0,1)
    :param N: number of needed implementations of the random variable
    :return: result list
    '''
    result = []
    for i in range(0, N):
        uniVar1 = np.random.uniform(0, 1, 1)
        uniVar2 = np.random.uniform(0, 1, 1)
        impl1 = m.sqrt(-2 * m.log(uniVar1, m.e)) * m.cos(2 * m.pi * uniVar2)
        impl2 = m.sqrt(-2 * m.log(uniVar1, m.e)) * m.sin(2 * m.pi * uniVar2)
        result.append(impl1)
        result.append(impl2)
    return result


def normalDistributionModeling2(N, n):
    '''
    This function returns a list of N implementations of the random variable which is based
    on the other random variable, for example, uniformly distributed on the (0,1)
    :param N: number of needed implementations of the random variable
    :param n: number needed in formula
    :return: result list
    '''
    result = []
    for i in range(0, N):
        sum = 0
        for i in range(0, n):
            sum += np.random.uniform(0, 1, 1) - 0.5
        impl = sum * m.sqrt(12.0 / n)
        result.append(impl)
    return result


# lets examine the histograms

model1 = normalDistributionModeling1(1000)
model2p1 = normalDistributionModeling2(1000, 3)
model2p2 = normalDistributionModeling2(1000, 12)
model2p3 = normalDistributionModeling2(1000, 48)

stat, p1 = stats.normaltest(model1)
stat, p2 = stats.normaltest(model2p1)
stat, p3 = stats.normaltest(model2p2)
stat, p4 = stats.normaltest(model2p3)

print("p-value for model1 = {}".format(p1))
print("p-value for model2p1 = {}".format(p2))
print("p-value for model2p2 = {}".format(p3))
print("p-value for model2p3 = {}".format(p4))
print('\n')
print("So, as we can see, the null hypothesis (our model comes from a normal "
      "distribution) is accepted for the model 1, and the model 2 with values "
      "of n=12 and n=48")
