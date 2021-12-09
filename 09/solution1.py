import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

input_list = []
x_size = 0
y_size = 0

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        line = [int(i) for i in line]
        input_list.append(line)
    x_size = len(line)
    y_size = len(input_list)

lowest_list = []

for i in range(y_size):
    for j in range(x_size):
        check_list = []
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
            lowest_list.append(target)

sum_of_risk_levels = sum([i + 1 for i in lowest_list])

print(f"Sum of risk levels: {sum_of_risk_levels}")
