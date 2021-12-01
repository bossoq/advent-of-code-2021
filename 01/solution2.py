import numpy as np

input_arr = np.loadtxt('input.txt')

input_arr_l0 = input_arr[:-2]
input_arr_l1 = input_arr[1:-1]
input_arr_l2 = input_arr[2:]

sum_3window_arr = np.add(np.add(input_arr_l0, input_arr_l1), input_arr_l2)

sum_3window_arr_l0 = sum_3window_arr[:-1]
sum_3window_arr_l1 = sum_3window_arr[1:]

output_arr = np.subtract(sum_3window_arr_l1, sum_3window_arr_l0)

print(f"Solution is : {np.sum(output_arr > 0)}")
