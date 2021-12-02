import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

h_pos = 0
d_pos = 0
aim = 0

with open(input_file, "r") as f:
    for line in f:
        command = line.strip().split()
        step = command[0]
        distance = int(command[1])
        if step == "forward":
            h_pos += distance
            d_pos += distance * aim
        elif step == "down":
            aim += distance
        elif step == "up":
            aim -= distance

print(
    f"Submarine ends up at {h_pos} and {d_pos} (aim: {aim}) ({h_pos * d_pos})")
