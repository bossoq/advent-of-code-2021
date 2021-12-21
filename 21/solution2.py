import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print('Usage: python solution2.py <input_file>')
    exit(1)

input_list = list()

with open(input_file, 'r') as f:
    for line in f:
        input_list.append(int(line.strip().split(': ')[1]))


wins = dict()


def game_rolled(pos, count, cur_player):
    data = (pos[0], pos[1], count[0], count[1], cur_player)
    if data in wins:
        return wins[data]
    if count[0] >= 21:
        return [1, 0]
    if count[1] >= 21:
        return [0, 1]

    steps = [
        [3, 1],
        [4, 3],
        [5, 6],
        [6, 7],
        [7, 6],
        [8, 3],
        [9, 1]
    ]

    round_wins = [0, 0]

    for step, multiple in steps:
        orig_pos = pos[cur_player]
        new_pos = ((orig_pos + step - 1) % 10) + 1
        pos[cur_player] = new_pos
        count[cur_player] += new_pos
        next_player = (cur_player + 1) % 2

        ret = game_rolled(pos, count, next_player)
        round_wins[0] += multiple * ret[0]
        round_wins[1] += multiple * ret[1]

        pos[cur_player] = orig_pos
        count[cur_player] -= new_pos

    wins[data] = round_wins
    return round_wins


result = game_rolled(input_list, [0, 0], 0)
print(f'Player 1 wins {result[0]} times')
print(f'Player 2 wins {result[1]} times')
print(f'Max wins: {max(result)}')

'''
1 1 1 = 3
1 1 2 = 4
1 1 3 = 5

1 2 1 = 4
1 2 2 = 5
1 2 3 = 6

1 3 1 = 5
1 3 2 = 6
1 3 3 = 7

2 1 1 = 4
2 1 2 = 5
2 1 3 = 6

2 2 1 = 5
2 2 2 = 6
2 2 3 = 7

2 3 1 = 6
2 3 2 = 7
2 3 3 = 8

3 1 1 = 5
3 1 2 = 6
3 1 3 = 7

3 2 1 = 6
3 2 2 = 7
3 2 3 = 8

3 3 1 = 7
3 3 2 = 8
3 3 3 = 9
'''

'''
3 1
4 3
5 6
6 7
7 6
8 3
9 1
'''
