import numpy as np
from matplotlib import pyplot as plt


def maxUniList(N, n):
    '''
    Generates a list of N implementations of the random variable f = max{k1,k2,...,kn}, where
    ki (i=1..n) is the implementation of the uniform random variable with the standard uniform
    distribution (0,1). Obviously, the distribution function here is
    F(x) = {0 for x<=0; x^n for x in (0,1); 1 for x>=1}
    :param N: number of f-implementations
    :param n: number of k-implementations
    :return: result list
    '''
    result = []
    for i in range(0, N):
        uniList = np.random.uniform(0, 1, n)
        result.append(max(uniList))
    return result


maxUniListSample = maxUniList(2000, 100)
for i in maxUniListSample:
    print(i)

plt.xlim([min(maxUniListSample)-0.01, 1])
plt.hist(maxUniListSample, bins=100, alpha=1)
plt.title('MaxUniform(0,1) histogram')
plt.xlabel('MaxUniform(0,1) variable')
plt.ylabel('count')

plt.show()