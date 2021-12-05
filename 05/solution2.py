import sys

import numpy as np

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

coords = []
with open(input_file, "r") as f:
    for line in f:
        coordinates = line.strip().split(" -> ")
        start = coordinates[0].split(",")
        end = coordinates[1].split(",")
        coord = [start, end]
        coords.append(coord)

coords = np.array(coords).astype(int)

max_coord = coords.max()

mapped = np.zeros((max_coord + 1, max_coord + 1), dtype=int)

for coord in coords:
    # [2, 2] -> [2, 1]
    if coord[0][0] == coord[1][0]:
        first = min(coord[0][1], coord[1][1])
        second = max(coord[0][1], coord[1][1]) + 1
        mapped[first:second, coord[0][0]] += 1
    # [0, 9] -> [5, 9]
    elif coord[0][1] == coord[1][1]:
        first = min(coord[0][0], coord[1][0])
        second = max(coord[0][0], coord[1][0]) + 1
        mapped[coord[0][1], first:second] += 1
    # [8, 0] -> [0, 8]
    elif abs(coord[0][0] - coord[1][0]) == abs(coord[0][1] - coord[1][1]):
        for i in range(abs(coord[0][0] - coord[1][0]) + 1):
            if coord[0][0] > coord[1][0] and coord[0][1] > coord[1][1]:
                mapped[coord[0][1] - i, coord[0][0] - i] += 1
            elif coord[0][0] > coord[1][0] and coord[0][1] < coord[1][1]:
                mapped[coord[0][1] + i, coord[0][0] - i] += 1
            elif coord[0][0] < coord[1][0] and coord[0][1] > coord[1][1]:
                mapped[coord[0][1] - i, coord[0][0] + i] += 1
            elif coord[0][0] < coord[1][0] and coord[0][1] < coord[1][1]:
                mapped[coord[0][1] + i, coord[0][0] + i] += 1

total_overlap = (mapped > 1).sum()
print(mapped)
print(f"Total Overlap Point: {total_overlap}")
