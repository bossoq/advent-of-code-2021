from operator import mul
from functools import reduce
from collections import deque
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

input_list = list()
x_size = 0
y_size = 0

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        line = [int(i) for i in line]
        input_list.append(line)
    x_size = len(line)
    y_size = len(input_list)

basin_list = list()

for i in range(y_size):
    for j in range(x_size):
        check_list = list()
        target = input_list[i][j]
        if i > 0:
            check_list.append(input_list[i - 1][j])
        if j > 0:
            check_list.append(input_list[i][j - 1])
        if i < y_size - 1:
            check_list.append(input_list[i + 1][j])
        if j < x_size - 1:
            check_list.append(input_list[i][j + 1])

        if target < min(check_list):
            pos = list()
            processed = list()
            queue = deque()
            pos.append([i, j])
            queue.append([i, j])
            while len(queue) > 0:
                new_pos = queue.popleft()
                if new_pos not in processed:
                    processed.append(new_pos)
                    y, x = new_pos
                    if y > 0:
                        top_pos = [y - 1, x]
                        if top_pos not in processed:
                            top = input_list[y - 1][x]
                            if top < 9:
                                pos.append(top_pos)
                                queue.append(top_pos)
                    if y < y_size - 1:
                        bottom_pos = [y + 1, x]
                        if bottom_pos not in processed:
                            bottom = input_list[y + 1][x]
                            if bottom < 9:
                                pos.append(bottom_pos)
                                queue.append(bottom_pos)
                    if x > 0:
                        left_pos = [y, x - 1]
                        if left_pos not in processed:
                            left = input_list[y][x - 1]
                            if left < 9:
                                pos.append(left_pos)
                                queue.append(left_pos)
                    if x < x_size - 1:
                        right_pos = [y, x + 1]
                        if right_pos not in processed:
                            right = input_list[y][x + 1]
                            if right < 9:
                                pos.append(right_pos)
                                queue.append(right_pos)

            pos = [i for n, i in enumerate(pos) if i not in pos[:n]]
            basin = len(pos)
            basin_list.append(basin)

top_three_basin = sorted(basin_list, reverse=True)[:3]
multiply_of_basin = reduce(mul, top_three_basin)

print(f"Top Three Basin: {top_three_basin}")
print(f"Multiply of Top Three Basin: {multiply_of_basin}")
