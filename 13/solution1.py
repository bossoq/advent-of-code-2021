from collections import deque
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

input_list = list()
fold_step = deque()

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if 'fold along' in line:
            line = line.replace("fold along ", "")
            line = line.split("=")
            fold_step.append([line[0], int(line[1])])
        elif len(line) > 0:
            line = line.split(",")
            input_list.append(int(line[0]) + 1j * int(line[1]))

output_list = set(input_list)

i = 1
while len(fold_step) > 0:
    step = fold_step.popleft()
    previous_list = output_list.copy()
    output_list = set()
    if step[0] == "y":
        for pos in previous_list:
            if pos.imag > step[1]:
                delta = (pos.imag - step[1])
                pos -= delta * 2j
            output_list.add(pos)
    if step[0] == "x":
        for pos in previous_list:
            if pos.real > step[1]:
                delta = (pos.real - step[1])
                pos -= delta * 2
            output_list.add(pos)
    print(f"Step {i}: {len(output_list)}")
    i += 1
