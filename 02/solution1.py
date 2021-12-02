import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

h_pos = 0
d_pos = 0

with open(input_file, "r") as f:
    for line in f:
        command = line.strip().split()
        step = command[0]
        distance = int(command[1])
        if step == "forward":
            h_pos += distance
        elif step == "down":
            d_pos += distance
        elif step == "up":
            d_pos -= distance

print(f"Submarine ends up at {h_pos} and {d_pos} ({h_pos * d_pos})")
