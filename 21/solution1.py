from collections import deque
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print('Usage: python solution1.py <input_file>')
    exit(1)

input_list = list()

with open(input_file, 'r') as f:
    for line in f:
        input_list.append(int(line.strip().split(': ')[1]))


dice = deque(list(range(1, 101)))


def get_dice():
    dists = list()
    dists.append(dice.popleft())
    dists.append(dice.popleft())
    dists.append(dice.popleft())
    for dist in dists:
        dice.append(dist)
    return sum(dists)


def game_rolled(pos, count):
    dists = get_dice()
    pos = (pos + dists - 1) % 10 + 1
    count += pos
    return pos, count


p1_pos, p2_pos = input_list
p1_count = p2_count = 0
rolled = 0

while True:
    p1_pos, p1_count = game_rolled(p1_pos, p1_count)
    rolled += 3
    if p1_count >= 1000:
        break

    p2_pos, p2_count = game_rolled(p2_pos, p2_count)
    rolled += 3
    if p2_count >= 1000:
        break

if p1_pos > p2_pos:
    print(f'Winner: Player 1 {p1_count}')
    print(f'Loser : Player 2 {p2_count}')
    print(f'Total Rolled: {rolled}')
    print(f'Loser * Rolled: {p2_count * rolled}')
else:
    print(f'Winner: Player 2 {p2_count}')
    print(f'Loser : Player 1 {p1_count}')
    print(f'Total Rolled: {rolled}')
    print(f'Loser * Rolled: {p1_count * rolled}')
