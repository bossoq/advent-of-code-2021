import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

with open(input_file, "r") as f:
    input_list = f.readline().split(",")
    input_list = [int(i) for i in input_list]

min_horizontal = min(input_list)
max_horizontal = max(input_list)

minimum_distance = int(min(sum((abs(v - i) * (abs(v - i) + 1)) / 2 for v in input_list)
                       for i in range(min_horizontal, max_horizontal + 1)))

print(f"Minimum fuel: {minimum_distance}")
