from collections import deque
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print('Usage: python solution2.py <input_file>')
    exit(1)

input = ''

with open(input_file, 'r') as f:
    input = f.readline().strip()


opcodes = {
    ('0', '0', '0'): 'sum',
    ('0', '0', '1'): 'product',
    ('0', '1', '0'): 'min',
    ('0', '1', '1'): 'max',
    ('1', '0', '1'): 'gt',
    ('1', '1', '0'): 'lt',
    ('1', '1', '1'): 'eq'
}


def generate_bits(hexa, pos, nbr):
    result = []
    char_pos = pos // 4
    bit_pos = pos % 4
    while len(result) < nbr:
        char = hexa[char_pos]
        bits = f'{int(char, 16):04b}'
        while len(result) < nbr and bit_pos < 4:
            result.append(bits[bit_pos])
            bit_pos += 1
        if bit_pos == 4:
            char_pos += 1
            bit_pos = 0
    return result, char_pos * 4 + bit_pos


def check_type(oper, pos):
    if oper['length_type'] == 'packets':
        read_packets = len(oper['value'])
        if read_packets == oper['n_packets']:
            return True
        elif read_packets > oper['n_packets']:
            print(f'Error: Too many packets read at position {pos}')
            exit(1)
    elif oper['length_type'] == 'bits':
        read_bits = pos - oper['sub_pos']
        if read_bits == oper['n_bits']:
            return True
        elif read_bits > oper['n_bits']:
            print(f'Error: Too many bits read at position {pos}')
            exit(1)


def calculator(oper):
    if isinstance(oper, int):
        return oper

    op_type = oper['op']
    values = [calculator(x) for x in oper['value']]
    if len(values) == 0:
        print(f'Calc Error: {oper}')
        exit(1)

    if op_type == 'sum':
        return sum(values)
    elif op_type == 'product':
        result = 1
        for value in values:
            result *= value
        return result
    elif op_type == 'min':
        return min(values)
    elif op_type == 'max':
        return max(values)
    elif op_type == 'gt':
        if values[0] > values[1]:
            return 1
        return 0
    elif op_type == 'lt':
        if values[0] < values[1]:
            return 1
        return 0
    elif op_type == 'eq':
        if values[0] == values[1]:
            return 1
        return 0


def parse_hexa(hexa):
    max_bit_len = len(hexa * 4)
    min_hexa_len = 7
    sub_packet = False
    pos = 0

    read_bits = 0
    sub_packet_count = 0

    stack = deque()

    while pos < max_bit_len - min_hexa_len:
        start_pos = pos
        literal_value_list = list()
        version, pos = generate_bits(hexa, pos, 3)

        type_id, pos = generate_bits(hexa, pos, 3)
        if type_id == ['1', '0', '0']:
            number, pos = generate_bits(hexa, pos, 5)
            literal_value_list.append(str(''.join(number[1:])))
            while number[0] == '1':
                number, pos = generate_bits(hexa, pos, 5)
                literal_value_list.append(str(''.join(number[1:])))
            if not sub_packet:
                break
            read_bits += pos - start_pos
            sub_packet_count += 1
            number_convert = int(str(''.join(literal_value_list)), 2)
            stack[-1]['value'].append(number_convert)
        else:
            oper = {
                'op': opcodes[tuple(type_id)],
                'value': [],
                'start_pos': start_pos,
                'sub_pos': -1,
                'n_packets': -1,
                'n_bits': -1
            }
            if len(stack) > 0:
                stack[-1]['value'].append(oper)
            stack.append(oper)
            length_type, pos = generate_bits(hexa, pos, 1)
            sub_packet = True
            if length_type[0] == '0':
                n_bits, pos = generate_bits(hexa, pos, 15)
                stack[-1]['n_bits'] = int(str(''.join(n_bits)), 2)
                stack[-1]['sub_pos'] = pos
                stack[-1]['length_type'] = 'bits'
            elif length_type[0] == '1':
                n_packet, pos = generate_bits(hexa, pos, 11)
                stack[-1]['n_packets'] = int(str(''.join(n_packet)), 2)
                stack[-1]['length_type'] = 'packets'

        while len(stack) > 1 and check_type(stack[-1], pos):
            oper = stack.pop()

    while len(stack) > 1:
        stack.pop()

    return calculator(stack.pop())


result = parse_hexa(input)
print(f"Calculation Result: {result}")
