import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
    exit(1)

image_enhancement_algorithm = ''
input_dict = dict()

with open(input_file, "r") as f:
    for ridx, row in enumerate(f):
        if ridx == 0:
            image_enhancement_algorithm = row.strip()
        elif ridx > 1:
            for cidx, col in enumerate(row.strip()):
                input_dict[cidx + 1j * (ridx - 2)] = col
    col_count = len(row)
    row_count = int(len(input_dict) / col_count)


def apply_enhancement(pos, inp_image, algorithm, iteration):
    deltas = (-1 - 1j, -1j, 1 - 1j, -1, 0, 1, -1 + 1j, 1j, 1 + 1j)
    binary_string = ''
    for d in deltas:
        if iteration % 2 == 1 and algorithm[0] == '#':
            binary_string += inp_image.get(pos + d,
                                           '#').replace('#', '1').replace('.', '0')
        else:
            binary_string += inp_image.get(pos + d,
                                           '.').replace('#', '1').replace('.', '0')
    decimal_idx = int(binary_string, 2)
    ret = algorithm[decimal_idx]
    return ret


def loop_through_input(inp, iteration, iterations):
    ret_dict = dict()
    for y in range(-iterations, row_count + iterations):
        for x in range(-iterations, col_count + iterations):
            pos = x + 1j * y
            ret_dict[pos] = apply_enhancement(
                pos, inp, image_enhancement_algorithm, iteration)
    return ret_dict


def print_image(inp, iterations):
    count = 0
    for y in range(-iterations, col_count + iterations):
        for x in range(-iterations, row_count + iterations):
            pixel = inp[x + 1j * y]
            if pixel == '#':
                count += 1
            print(pixel, end='')
        print()
    return count


output_dict = input_dict
loop = 50
for i in range(loop):
    output_dict = loop_through_input(output_dict, i, loop)
pixel_count = print_image(output_dict, loop)
print(f'Total Pixel lit: {pixel_count}')
