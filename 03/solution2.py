import sys

import numpy as np

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

arr = []
with open(input_file, "r") as f:
    for line in f:
        arr.append([int(char) for char in line.strip()])

bit_len = len(arr[0])

o2_arr = np.array(arr)
o2_len = bit_len
i = 0
while o2_len > 1:
    o2_arr_num = len(o2_arr)
    o2_arr_half = o2_arr_num / 2
    o2_arr_trans = o2_arr.transpose()
    if sum(o2_arr_trans[i]) >= o2_arr_half:
        o2_arr = o2_arr[(o2_arr_trans[i] == 1).transpose()]
    else:
        o2_arr = o2_arr[(o2_arr_trans[i] == 0).transpose()]
    o2_len = len(o2_arr)
    i += 1

o2_int = int(''.join(o2_arr[0].astype(int).astype(str).tolist()), 2)

co2_arr = np.array(arr)
co2_len = bit_len
i = 0
while co2_len > 1:
    co2_arr_num = len(co2_arr)
    co2_arr_half = co2_arr_num / 2
    co2_arr_trans = co2_arr.transpose()
    if sum(co2_arr_trans[i]) >= co2_arr_half:
        co2_arr = co2_arr[(co2_arr_trans[i] == 0).transpose()]
    else:
        co2_arr = co2_arr[(co2_arr_trans[i] == 1).transpose()]
    co2_len = len(co2_arr)
    i += 1

co2_int = int(''.join(co2_arr[0].astype(int).astype(str).tolist()), 2)

print(
    f"O2 Generator Rating: {o2_int}, CO2 Scrubber Rating: {co2_int}, Life Support Rating: {o2_int * co2_int}")
