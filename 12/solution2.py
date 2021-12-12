from collections import deque, Counter
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

input_dict = dict()
input_set = set()

with open(input_file, "r") as f:
    for line in f:
        line = line.strip().split("-")
        if line[0] not in ["start", "end"]:
            input_set.add(line[0])
        if line[1] not in ["start", "end"]:
            input_set.add(line[1])
        if line[0] != "end" and line[1] != "start":
            try:
                input_dict[line[0]].append(line[1])
            except KeyError:
                input_dict[line[0]] = [line[1]]
        if line[1] != "end" and line[0] != "start":
            try:
                input_dict[line[1]].append(line[0])
            except KeyError:
                input_dict[line[1]] = [line[0]]

start_path = [["start", p] for p in input_dict.get("start")]

output_paths = list()
queue = deque(start_path)

while len(queue) > 0:
    current_path = queue.popleft()
    previous_node = current_path[-1]
    if previous_node == "end":
        output_paths.append(current_path)
    else:
        counter = Counter(current_path)
        max_lower = False
        for k, v in counter.items():
            if k.islower() and k != "start" and v == 2:
                max_lower = True
        for node in input_dict.get(previous_node):
            if node.islower() and max_lower:
                if node not in current_path:
                    next_path = current_path + [node]
                    if next_path not in queue:
                        queue.append(next_path)
            else:
                next_path = current_path + [node]
                if next_path not in queue:
                    queue.append(next_path)

print(f"Total possible paths: {len(output_paths)}")
