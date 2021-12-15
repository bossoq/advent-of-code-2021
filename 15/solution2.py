import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

input_dict = dict()

with open(input_file, "r") as f:
    for ridx, row in enumerate(f):
        for cidx, col in enumerate(row.strip()):
            input_dict[cidx + 1j * ridx] = int(col)
    col_count = len(row)
    row_count = int(len(input_dict) / col_count)


def get_neighbors(pos):
    neighbors = []
    if pos.real > 0:
        neighbors.append(pos.real - 1 + pos.imag * 1j)
    if pos.real < 5 * col_count - 1:
        neighbors.append(pos.real + 1 + pos.imag * 1j)
    if pos.imag > 0:
        neighbors.append(pos.real + (pos.imag - 1) * 1j)
    if pos.imag < 5 * row_count - 1:
        neighbors.append(pos.real + (pos.imag + 1) * 1j)
    return neighbors


def get_value(input_dict, pos):
    x = pos.real % col_count
    y = pos.imag % row_count
    extra = (pos.real // col_count) + (pos.imag // row_count)
    result = int(((input_dict[x + 1j * y] + extra) %
                 10) + ((input_dict[x + 1j * y] + extra) // 10))
    return result


def main():
    dists = dict()
    tovisit = set()
    tovisit.add(0 + 0j)
    visited = set()
    dists[0 + 0j] = 0

    while len(tovisit) > 0:
        node = sorted(tovisit, key=lambda x: dists[x])[0]
        tovisit.remove(node)
        visited.add(node)

        for neighbor in get_neighbors(node):
            nextdist = dists[node] + get_value(input_dict, neighbor)
            if neighbor not in visited and dists.get(neighbor, 10000000) > nextdist:
                dists[neighbor] = nextdist
                tovisit.add(neighbor)
    return dists[5 * col_count - 1 + (5 * row_count - 1) * 1j]


risk_level = main()
print(f"Lowest Risk Level: {risk_level}")
