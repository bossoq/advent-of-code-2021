from collections import Counter
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

input_list = []

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        input_list.append(line)

close_bracket_list = [")", ">", "]", "}"]
score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def remove_closer_bracket(line):
    line_len = len(line)
    old_line_len = 0
    while line_len != old_line_len:
        line = line.replace("()", "")
        line = line.replace("<>", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        old_line_len = line_len
        line_len = len(line)
    return line


clean_line_list = list()
for line in input_list:
    clean_line = remove_closer_bracket(line)
    clean_line_list.append(clean_line)

sum_score = 0
for idx, line in enumerate(clean_line_list):
    counter = Counter(line)
    illegal_line = counter.get(")", 0) + counter.get(">", 0) + \
        counter.get("]", 0) + counter.get("}", 0)
    if illegal_line > 0:
        bracket_list = list(counter.keys())
        for bracket in bracket_list:
            if bracket in close_bracket_list:
                sum_score += score.get(bracket)
                break

print(f"Total Syntax Error Score: {sum_score}")
