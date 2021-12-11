from collections import deque
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

input_dict = dict()

with open(input_file, "r") as f:
    for ridx, row in enumerate(f):
        for cidx, col in enumerate(row.strip()):
            input_dict[cidx + 1j * ridx] = int(col)

loop = 100
total_flashed = 0

for i in range(loop):
    input_dict = {k: v + 1 for k, v in input_dict.items()}
    flashed = set()
    queue = deque()
    for pos, energy in input_dict.items():
        if energy > 9:
            queue.append(pos)
    while len(queue) > 0:
        new_pos = queue.popleft()
        if new_pos not in flashed:
            for d in (-1, -1 - 1j, -1j, 1 - 1j, 1, 1 + 1j, 1j, -1 + 1j):
                try:
                    input_dict[new_pos + d] += 1
                    if input_dict[new_pos + d] > 9:
                        queue.append(new_pos + d)
                except KeyError:
                    pass
            flashed.add(new_pos)
    input_dict = {k: 0 if v > 9 else v for k, v in input_dict.items()}
    total_flashed += len(flashed)

print(f"Total Flashed: {total_flashed}")
