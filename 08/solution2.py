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

'''
[1, 4, 7, 8] has unique counts = [2, 4, 3, 7]
[2, 3, 5] has same 5 counts
[0, 1, 9] has same 6 counts
'''

'''
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
8       5     2     3     7   9      6      4    0      1
a == d
c == a
f == b
b == e
d == f
g == c
e == g

'''

# List of 1, 4, 7 and 8 counts
segments = [2, 4, 3, 7]

try:
    input_file = sys.argv[1]
except IndexError:
    print("Usage: python solution2.py <input_file>")
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


def decode(unique_list):
    two_three_five = []
    zero_six_nine = []
    # Find 1, 4, 7 and 8 since it has unique counts and filter 2, 3, 5 and 0, 6, 9
    for string in unique_list:
        if len(string) == 2:
            tmp = list(string)
            tmp.sort()
            one = "".join(tmp)
        elif len(string) == 4:
            tmp = list(string)
            tmp.sort()
            four = "".join(tmp)
        elif len(string) == 3:
            tmp = list(string)
            tmp.sort()
            seven = "".join(tmp)
        elif len(string) == 7:
            tmp = list(string)
            tmp.sort()
            eight = "".join(tmp)
        elif len(string) == 5:
            two_three_five.append(string)
        elif len(string) == 6:
            zero_six_nine.append(string)

    # Find 9 since 4 is subset of 9 with 6 counts
    for string in zero_six_nine:
        if all(char in string for char in four):
            tmp = list(string)
            tmp.sort()
            nine = "".join(tmp)
            zero_six = zero_six_nine.copy()
            zero_six.remove(string)

    # Find 3 since 7 is subset of 3 with 5 counts
    for string in two_three_five:
        if all(char in string for char in seven):
            tmp = list(string)
            tmp.sort()
            three = "".join(tmp)
            two_five = two_three_five.copy()
            two_five.remove(string)

    # Find 0 since 1 is subset of 0 with 6 counts
    for string in zero_six:
        if all(char in string for char in one):
            tmp = list(string)
            tmp.sort()
            zero = "".join(tmp)
        else:
            tmp = list(string)
            tmp.sort()
            six = "".join(tmp)

    # Find 5 since 5 is subset of 9 with 5 counts
    for string in two_five:
        if all(char in nine for char in string):
            tmp = list(string)
            tmp.sort()
            five = "".join(tmp)
        else:
            tmp = list(string)
            tmp.sort()
            two = "".join(tmp)
    return [zero, one, two, three, four, five, six, seven, eight, nine]


def decode_string(output, decode_list):
    output_decoded = ""
    zero, one, two, three, four, five, six, seven, eight, nine = decode_list
    for string in output:
        sorted_string = list(string)
        sorted_string.sort()
        sorted_string = "".join(sorted_string)
        if sorted_string == zero:
            output_decoded += "0"
        elif sorted_string == one:
            output_decoded += "1"
        elif sorted_string == two:
            output_decoded += "2"
        elif sorted_string == three:
            output_decoded += "3"
        elif sorted_string == four:
            output_decoded += "4"
        elif sorted_string == five:
            output_decoded += "5"
        elif sorted_string == six:
            output_decoded += "6"
        elif sorted_string == seven:
            output_decoded += "7"
        elif sorted_string == eight:
            output_decoded += "8"
        elif sorted_string == nine:
            output_decoded += "9"
    return int(output_decoded)


outputs_decoded = 0
for line in input_list:
    decode_list = decode(line[0])
    output_decoded = decode_string(line[1], decode_list)
    outputs_decoded += output_decoded

print(f"Add all output values: {outputs_decoded}")
