import numpy as np


def pseudorandomBinarySeq(N):
    '''
    Generates list of N pseudorandom binary numbers using variables from the
    standard uniform distribution
    :param N: length of the list
    :return: list
    '''
    uniList = np.random.uniform(0, 1, N)
    result = []
    for i in range(0, N):
        if (uniList[i] < 0.5):
            result.append(0)
        else:
            result.append(1)
    return result

randBinList = pseudorandomBinarySeq(1000)
for i in randBinList:
    print(i)