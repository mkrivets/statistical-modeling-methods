import numpy as np

def distance(dot1, dot2):
    return np.sqrt(pow(dot1[0]-dot2[0], 2)+pow(dot1[1]-dot2[1], 2))

dots = [[7, 8], [12, 8], [14, 6], [14, 3], [14, -1], [14, -4.5], [10.7, -6], [3.7, -6],
        [-4.3, -6], [-11.3, -6], [-14, -5], [-14, -1.5], [-14, 3], [-14, 6.7],
        [-11.3, 8], [-4.7, 8], [1.3, 8], [-9.2, 1.6], [-6, 3],
        [-3, 4], [-1, 5], [1, -2.7], [4, -1.5],
        [7, -0.5], [9.3, 0.5]]
blocks = []
blocks.append(0)
for i in range(0, 7):
    flag = True
    while flag:
        temp = np.random.randint(1,25)
        if temp not in blocks:
            flag = False
            blocks.append(temp)

print(blocks)
passed = []
passed.append(0)
current = 0
while (len(passed) < 8):
    minDist = 1000
    minBlock = 0
    for i in blocks:
        if i not in passed:
            dist = distance(dots[i], dots[current])
            if minDist > dist:
                minDist = dist
                minBlock = i
    current = minBlock
    passed.append(current)

print(passed)

