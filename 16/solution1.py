import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print('Usage: python solution1.py <input_file>')
    exit(1)

input = ''

with open(input_file, 'r') as f:
    input = f.readline().strip()


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


def parse_hexa(hexa):
    version_total = 0
    max_bit_len = len(hexa * 4)
    min_hexa_len = 7
    sub_packet = False
    pos = 0

    read_bits = 0
    sub_packet_count = 0

    while pos < max_bit_len - min_hexa_len:
        start_pos = pos
        literal_value_list = list()
        version, pos = generate_bits(hexa, pos, 3)

        version_total += int(str(''.join(version)), 2)

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
        else:
            length_type, pos = generate_bits(hexa, pos, 1)
            sub_packet = True
            if length_type[0] == '0':
                n_bits, pos = generate_bits(hexa, pos, 15)
            elif length_type[0] == '1':
                n_packet, pos = generate_bits(hexa, pos, 11)
            else:
                exit(1)

    return version_total


version_total = parse_hexa(input)
print(f"Version total: {version_total}")
