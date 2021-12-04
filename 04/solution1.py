import sys

import numpy as np

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

first_line = True
draw = []
boards = []
board = []
with open(input_file, "r") as f:
    count = 0
    row_len = -1
    for line in f:
        line = line.rstrip()
        line_len = len(line)
        if first_line:
            first_line = False
            draw = line.split(",")
        elif line_len > 0:
            row = line.split()
            row_len = len(row)
            board.append(row)
            count += 1
        if count == row_len:
            boards.append(board)
            board = []
            count = 0

boards_arr = np.array(boards)

i = 0
for num in draw:
    i += 1
    try:
        marked_boards += boards_arr == num
    except NameError:
        marked_boards = boards_arr == num
    j = 0
    for marked_board in marked_boards:
        h_sum = np.sum(marked_board, axis=1)
        v_sum = np.sum(marked_board, axis=0)
        if (h_sum == row_len).sum() == 1 or (v_sum == row_len).sum() == 1:
            sum_unmarked = boards_arr[j][~marked_board].astype(int).sum()
            print("Found a winner!")
            print(f"Round: {i}")
            print(f"Last Drawn: {num}")
            print(f"Sum Unmarked: {sum_unmarked}")
            print(f"Final Score = {sum_unmarked * int(num)}")
            exit(0)
        j += 1
