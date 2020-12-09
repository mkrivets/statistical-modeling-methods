import numpy as np


def check_num_of_types(n):
    i0 = num_of_types_dist[0]
    i1 = i0 + num_of_types_dist[1]
    i2 = i1 + num_of_types_dist[2]
    i3 = i2 + num_of_types_dist[3]
    i4 = i3 + num_of_types_dist[4]
    if (n >= 0 and n < i0):
        return num_of_types[0]
    if (n >= i0 and n < i1):
        return num_of_types[1]
    if (n >= i1 and n < i2):
        return num_of_types[2]
    if (n >= i2 and n < i3):
        return num_of_types[3]
    if (n >= i3 and n <= i4):
        return num_of_types[4]

def check_types(n):
    i0 = types_dist[0]
    i1 = i0 + types_dist[1]
    i2 = i1 + types_dist[2]
    i3 = i2 + types_dist[3]
    i4 = i3 + types_dist[4]
    i5 = i4 + types_dist[5]
    i6 = i5 + types_dist[6]
    if (n >= 0 and n < i0):
        return types[0]
    if (n >= i0 and n < i1):
        return types[1]
    if (n >= i1 and n < i2):
        return types[2]
    if (n >= i2 and n < i3):
        return types[3]
    if (n >= i3 and n < i4):
        return types[4]
    if (n >= i4 and n < i5):
        return types[5]
    if (n >= i5 and n <= i6):
        return types[6]


def check_nums(n):
    i0 = nums_dist[0]
    i1 = i0 + nums_dist[1]
    i2 = i1 + nums_dist[2]
    i3 = i2 + nums_dist[3]
    i4 = i3 + nums_dist[4]
    i5 = i4 + nums_dist[5]
    i6 = i5 + nums_dist[6]
    if (n >= 0 and n < i0):
        return nums[0]
    if (n >= i0 and n < i1):
        return nums[1]
    if (n >= i1 and n < i2):
        return nums[2]
    if (n >= i2 and n < i3):
        return nums[3]
    if (n >= i3 and n < i4):
        return nums[4]
    if (n >= i4 and n < i5):
        return nums[5]
    if (n >= i5 and n <= i6):
        return nums[6]


rand_nums = [0.967, 0.489, 0.511, 0.137, 0.742, 0.017, 0.060, 0.706, 0.853, 0.179, 0.860]
num_of_types_dist = [0.202, 0.212, 0.221, 0.109, 0.255]
num_of_types = [1, 2, 3, 4, 5]
types_dist = [0.164, 0.099, 0.181, 0.059, 0.122, 0.062, 0.313]
types = ['автомат', 'ніж', 'кулемет', 'пістолет', 'гвинтівка', 'булава', 'граната']
nums_dist = [0.076, 0.105, 0.088, 0.068, 0.014, 0.043, 0.606]
nums = [1, 2, 3, 4, 5, 6, 7]

rand_num = rand_nums[np.random.randint(11)]
weapon_types_num = check_num_of_types(rand_num)
print("Кількість видів зброї: ", weapon_types_num)
weapon_types = []

for i in range(0, weapon_types_num):
    flag = True
    while flag:
        rand_num = rand_nums[np.random.randint(11)]
        weapon_type = check_types(rand_num)
        if weapon_type not in weapon_types:
            weapon_types.append(weapon_type)
            flag = False
    rand_num = rand_nums[np.random.randint(11)]
    num_of_weapons = check_nums(rand_num)
    print('Кількість зброї виду {0}: {1}'.format(weapon_type, num_of_weapons))