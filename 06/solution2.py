import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

old_timer = 6
new_timer = 8

total_day = 256

with open(input_file, "r") as f:
    input_list = f.readline().split(",")
    input_list = [int(i) for i in input_list]

all_counts = [0] * (new_timer + 1)

for initial in input_list:
    all_counts[initial] += 1
for day in range(total_day):
    current = all_counts.pop(0)
    all_counts[old_timer] += current
    all_counts.append(current)

lanternfish_count = sum(all_counts)
print(f"Total lanternfish count: {lanternfish_count}")
