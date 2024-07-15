# main.py

from color_utils import get_color_from_pair_number, get_pair_number_from_color

if __name__ == '__main__':
    pair_number = 4
    major_color, minor_color = get_color_from_pair_number(pair_number)
    print(f"Pair number {pair_number} corresponds to: {major_color}-{minor_color}")

    major_color = 'Black'
    minor_color = 'Orange'
    pair_number = get_pair_number_from_color(major_color, minor_color)
    print(f"Pair {major_color}-{minor_color} corresponds to pair number: {pair_number}")
