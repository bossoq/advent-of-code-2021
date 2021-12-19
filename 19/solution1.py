import copy
import sys
from collections import deque

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

all_input = list()

with open(input_file, "r") as f:
    input_list = list()
    for line in f:
        input = line.strip().split(",")
        if ',' in line:
            input_list.append(tuple([int(pos) for pos in input]))
        else:
            if len(input_list) > 0:
                all_input.append(input_list)
            input_list = list()
    if len(input_list) > 0:
        all_input.append(input_list)


def RotateX90(pos):
    return [pos[0], -pos[2], pos[1]]


def FlipX(pos):
    return [-pos[0], pos[1], -pos[2]]


def Y2X(pos):
    return [pos[1], -pos[0], pos[2]]


def Z2X(pos):
    return [pos[2], pos[1], -pos[0]]


def permutations(lst):
    ret = list()
    ret.append(lst)
    ret.append([Y2X(pos) for pos in lst])
    ret.append([Z2X(pos) for pos in lst])
    for ls in copy.deepcopy(ret):
        ret.append([FlipX(pos) for pos in ls])
    for ls in copy.deepcopy(ret):
        ret.append([RotateX90(pos) for pos in ls])
        ret.append([RotateX90(pos) for pos in ret[-1]])
        ret.append([RotateX90(pos) for pos in ret[-1]])
    return ret


def create_maps(file_input):
    beacons = set(file_input[0])
    scanners = set()
    queue = deque()
    for pos_lst in file_input[1:]:
        queue.append(permutations(pos_lst))
    while len(queue) > 0:
        pos_lst_perm = queue.popleft()
        found = False
        for pos_lst in pos_lst_perm:
            d = dict()
            for check_pos in pos_lst:
                for ref_pos in beacons:
                    delta = (ref_pos[0] - check_pos[0], ref_pos[1] -
                             check_pos[1], ref_pos[2] - check_pos[2])
                    if delta in d.keys():
                        d[delta] += 1
                    else:
                        d[delta] = 1
            sorted_d = {k: v for k, v in sorted(
                d.items(), key=lambda item: item[1])}
            d = list(sorted_d.keys())[-1]
            n = list(sorted_d.values())[-1]
            if n >= 12:
                for pos in pos_lst:
                    beacons.add((pos[0] + d[0], pos[1] + d[1], pos[2] + d[2]))
                scanners.add(d)
                found = True
                break
        if not found:
            queue.append(pos_lst_perm)
    return beacons, scanners


beacons, scanners = create_maps(all_input)
print(f'Beacons count: {len(beacons)}')
