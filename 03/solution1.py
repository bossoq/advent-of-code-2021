import sys

import numpy as np

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

arr = []
with open(input_file, "r") as f:
    for line in f:
        arr.append([int(char) for char in line.strip()])

arr_num = len(arr)
arr_half = arr_num / 2
arr = np.array(arr)
arr_trans = arr.transpose()

bit_sum = arr_trans.sum(axis=1)
gamma_int = int(
    ''.join((bit_sum > arr_half).astype(int).astype(str).tolist()), 2)
epsilon_int = int(
    ''.join((bit_sum <= arr_half).astype(int).astype(str).tolist()), 2)

print(f"Gamma: {gamma_int}, Epsilon: {epsilon_int}, Power of Consumption: {gamma_int * epsilon_int}")
