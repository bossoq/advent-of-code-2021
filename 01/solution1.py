import sys

import numpy as np

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

try:
    input_arr = np.loadtxt(input_file)
except IOError:
    print("Error: Could not open file '{}'".format(input_file))
    exit(1)

input_arr_l0 = input_arr[:-1]
input_arr_l1 = input_arr[1:]

output_arr = np.subtract(input_arr_l1, input_arr_l0)

print(f"Solution is : {np.sum(output_arr > 0)}")
