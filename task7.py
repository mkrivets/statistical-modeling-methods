import numpy as np


def randomBinarySeq(N):
    '''
    Generates list of N random binary numbers based on the difference of 2 random variables.
    For example, uniformly distributed on the (0,1)
    :param N: length of the list
    :return: list
    '''
    uniList = np.random.uniform(0, 1, N + 1)
    result = []
    for i in range(0, N):
        if (uniList[i + 1] - uniList[i] > 0):
            result.append(1)
        else:
            result.append(0)
    return result


randBinList = randomBinarySeq(1000)
count0 = 0
for i in randBinList:
    print(i)
    if (i == 0):
        count0 += 1

print("The empirical distribution function is:")
print("F(x) = 0 for x<0")
print("{0} for 0<=x<1".format((count0 / len(randBinList))))
print("1 for x>=1")
