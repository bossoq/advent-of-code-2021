from collections import Counter
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

template = list()
pair_insertion = dict()
counter = dict()

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if "->" not in line and len(line) > 0:
            template_str = line
        elif "->" in line and len(line) > 0:
            pair = line.split(" -> ")[0].strip()
            insertion = line.split(" -> ")[1].strip()
            pair_insertion[pair] = insertion

counter[template_str[-1]] = 1
for i in range(len(template_str) - 1):
    template.append(template_str[i:i + 2])
template = dict(Counter(template))


def iter_insertion(template, pair_insertion):
    ret_template = dict()
    for k, count in template.items():
        left = k[0] + pair_insertion[k]
        right = pair_insertion[k] + k[1]

        try:
            ret_template[left] += count
        except KeyError:
            ret_template[left] = count
        try:
            ret_template[right] += count
        except KeyError:
            ret_template[right] = count
    return ret_template


iter_round = 40
for i in range(iter_round):
    template = iter_insertion(template, pair_insertion)

for k, count in template.items():
    char = k[0]
    try:
        counter[char] += count
    except KeyError:
        counter[char] = count

minimum = min(counter.values())
maximum = max(counter.values())
print(f"Most common subtract least common elemnt: {maximum - minimum}")
