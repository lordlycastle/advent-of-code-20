"""
Benchmark:
```
%time d1.part1(d1.raw)
634 + 1386 = 2020
CPU times: user 252 µs, sys: 32 µs, total: 284 µs
Wall time: 273 µs
Out[8]: 878724
%time d1.part2(d1.raw)
266 + 765 + 989 = 2020
CPU times: user 447 µs, sys: 29 µs, total: 476 µs
Wall time: 454 µs
Out[9]: 201251610
%time d1.check_sum(d1.data, 0, 1, 2020)
CPU times: user 10.5 ms, sys: 527 µs, total: 11 ms
Wall time: 10.5 ms
Out[10]: 878724
%time d1.check_sum(d1.data, 0, 2, 2020)
CPU times: user 1.35 s, sys: 6.06 ms, total: 1.36 s
Wall time: 1.36 s
Out[11]: 201251610
```
"""

import numpy as np
import helper
import runner

raw = runner.get_data(1)
argv = helper.str_to_array(raw)


def check_sum(data, current_sum, count, match):
    length = data.size
    for i in range(0, length):
        total_sum = current_sum + data[i]
        if count == 0:
            if total_sum == match:
                return data[i]
            else:
                continue
        else:
            found = check_sum(data, total_sum, count - 1, match)
            if found is not None:
                return found * data[i]
            else:
                continue


def part1(data):
    # Data is automatically read from 01.txt
    data = helper.sort_unique(argv)
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
    data = helper.sort_unique(argv)
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
