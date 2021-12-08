import sys

'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
'''

'''
0 = [a, b, c, e, f, g] = 6
1 = [c, f] = 2
2 = [a, c, d, e, g] = 5
3 = [a, c, d, f, g] = 5
4 = [b, c, d, f] = 4
5 = [a, b, d, f, g] = 5
6 = [a, b, d, e, f, g] = 6
7 = [a, c, f] = 3
8 = [a, b, c, d, e, f, g] = 7
9 = [a, b, c, d, f, g] = 6
'''

# List of 1, 4, 7 and 8 segments
segments = [2, 4, 3, 7]

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution1.py <input_file>")
    exit(1)

input_list = []

with open(input_file, "r") as f:
    for line in f:
        input_raw = line.strip().split(" | ")
        line_input = []
        for input_string in input_raw:
            input_split = input_string.split()
            line_input.append(input_split)
        input_list.append(line_input)

count = 0
for line_input in input_list:
    output_list = line_input[1]
    count += sum([len(string) in segments for string in output_list])

print(f"'1, 4, 7, 8' appear {count} times")
