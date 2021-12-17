import math
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print('Usage: python solution1.py <input_file>')
    exit(1)

target_area = list()

with open(input_file, 'r') as f:
    input = f.readline().strip().replace('target area: ', '').split(', ')
    x = input[0].replace('x=', '').split('..')
    y = input[1].replace('y=', '').split('..')
    target_area.append([int(x[0]), int(x[1])])
    target_area.append([int(y[0]), int(y[1])])


# Find min x step for y free fall
def find_max_x_step(target):
    min_x, max_x = target[0]
    for x in range(min_x, max_x - 1):
        min_step = (-1 + math.sqrt(1 + 8 * (x))) / 2
        if min_step.is_integer():
            min_step = int(min_step)
            break
    return min_step, x


def find_max_height(target, step_guess):
    max_height = 0

    min_y, max_y = target[1]
    max_y_speed = -min_y - 1
    y_step = 2 * (max_y_speed + 1)

    if step_guess <= y_step:
        max_height = int((max_y_speed * (max_y_speed + 1)) / 2)
    else:
        print(f"Cannot find max height for {step_guess}")

    return max_height


x_start, x = find_max_x_step(target_area)
max_height = find_max_height(target_area, x_start)
print(f"The maximum height is {max_height}")
