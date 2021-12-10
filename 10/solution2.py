from collections import Counter
import statistics
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

score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
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

total_score_list = list()
for idx, line in enumerate(clean_line_list):
    counter = Counter(line)
    illegal_line = counter.get(")", 0) + counter.get(">", 0) + \
        counter.get("]", 0) + counter.get("}", 0)
    if illegal_line == 0:
        line_score = 0
        count = len(line)
        for i in range(1, count + 1):
            line_score *= 5
            line_score += score.get(line[-i])
        total_score_list.append(line_score)

middle_score = statistics.median(total_score_list)

print(f"Middle Score: {middle_score}")
