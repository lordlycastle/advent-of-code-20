import numpy as np
import helper
import runner

raw = runner.get_data(1)


def find_sums(data, sum, count):
    length = len(data)
    np.zeros((length) * count)

def check_sum(data, current_sum, count, match):
    length = data.size
    for i in range(0, length):
        total_sum = current_sum + data[i]
        if count == 0:
            if total_sum == match:
                return data[i]
            else: continue
        else:
            check_sum(data, total_sum, count-1, match)


def part1(data):
    # Data is automatically read from 01.txt
    data = helper.sort_unique(helper.str_to_array(data))
    ans = 0
    length = data.size
    for i in range(0, length):
        for j in range(0, length):
            if i == j: continue
            sum = data[i] + data[j]
            if sum == 2020:
                print(f'{data[i]} + {data[j]} = {sum}')
                ans = data[i] * data[j]
                return ans

    print('No solution found.')


def part2(data):
    # Data is automatically read from 01.txt
    data = helper.sort_unique(helper.str_to_array(data))
    ans = 0
    length = data.size
    for i in range(0, length):
        for j in range(0, length):
            for k in range(0, length):
                if i == j or j == k or i == k: continue
                sum = data[i] + data[j] + data[k]
                if sum == 2020:
                    print(f'{data[i]} + {data[j]} + {data[k]} = {sum}')
                    ans = data[i] * data[j] * data[k]
                    return ans

    print('No solution found.')
