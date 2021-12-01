import numpy as np

input_arr = np.loadtxt('input.txt')

input_arr_l0 = input_arr[:-1]
input_arr_l1 = input_arr[1:]

output_arr = np.subtract(input_arr_l1, input_arr_l0)

print(f"Solution is : {np.sum(output_arr > 0)}")
