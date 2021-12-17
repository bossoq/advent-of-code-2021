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


def find_max_x(target):
    free_fall_x = list()
    min_x, max_x = target[0]
    for x in range(min_x, max_x - 1):
        min_step = (-1 + math.sqrt(1 + 8 * (x))) / 2
        if min_step.is_integer():
            min_step = int(min_step)
            free_fall_x.append(min_step)
    return min(free_fall_x), free_fall_x


def find_max_y_speed(target, step_guess):
    min_y, max_y = target[1]
    max_y_speed = -min_y - 1
    y_step = 2 * (max_y_speed + 1)

    if step_guess > y_step:
        print(f"Cannot find max height for {step_guess}")

    return max_y_speed


def find_min_max_step(target, x):
    all_step = list()
    min_x, max_x = target[0]
    count = dist = 0
    for i in reversed(range(x + 1)):
        count += 1
        dist += i
        if dist >= min_x and dist <= max_x:
            all_step.append(count)
        elif dist > max_x:
            break
    try:
        return min(all_step), max(all_step)
    except ValueError:
        return 0, 0


def find_min_max_y(target, min_step, max_step):
    min_y, max_y = target[1]

    init_min = sum(range(min_step))
    lower = -math.floor((-min_y - init_min) / min_step)

    init_max = sum(range(max_step))
    upper = -math.ceil((-max_y - init_max) / max_step)

    return lower, upper


def find_all_possible_velocity(target, min_x, free_fall_x, max_y):
    count = 0
    for x in range(min_x, target[0][1] + 1):
        min_step, max_step = find_min_max_step(target, x)
        if min_step > 0 and max_step > 0:
            lower_y, upper_y = find_min_max_y(target, min_step, max_step)

            # case free fall
            if x in free_fall_x:
                upper_y = max_y
                limit_lower_y = -find_min_max_y(target, 2, 2)[0]
                limit_upper_y = -target[1][1] - 2
                if limit_lower_y <= limit_upper_y:
                    local_count = limit_lower_y - lower_y + upper_y - limit_upper_y
                    count += local_count
                else:
                    local_count = upper_y - lower_y + 1
                    count += local_count
            # case 1 step to target
            elif x >= target[0][0]:
                lower_y, upper_y = target[1]
                local_count = upper_y - lower_y + 1
                count += local_count
            # case multiple steps to target
            else:
                local_count = upper_y - lower_y + 1
                count += local_count
    return count


min_x, free_fall_x = find_max_x(target_area)
max_y = find_max_y_speed(target_area, min_x)
count = find_all_possible_velocity(target_area, min_x, free_fall_x, max_y)

print(f'All possible velocity: {count}')
