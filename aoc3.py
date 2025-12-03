import pathlib
from typing import Optional

with pathlib.Path('/Users/ivana/aoc/2025/3/input.txt').open('r') as f:
    lines = f.readlines()


def find_max_index(chars: list[str], start: Optional[int] = None, end: Optional[int] = None) -> tuple[str, int]:
    if not start:
        start = 0
    if not end:
        end = len(chars)
    current_max = chars[start]
    current_max_index = start
    for i in range(start, end):
        if chars[i] > current_max:
            current_max = chars[i]
            current_max_index = i
    return current_max, current_max_index


################## PART 1 #################
sum = 0

for line in lines:
    line = line.strip()
    first_char, first_char_index = find_max_index(list(line[0:-1]))
    second_char, _ = find_max_index(list(line), start=first_char_index + 1)
    number = int(first_char + second_char)
    print(number)
    sum = sum + number

print(f'Part 1: {sum}')

################## PART 2 #################
sum = 0
digit_count = 12

for line in lines:
    line = line.strip()
    chars = []

    current_char_index = -1

    for i in range(digit_count):
        start_index = current_char_index + 1
        end_range_index = len(line) - digit_count + i + 1
        current_char, current_char_index = find_max_index(list(line), start=start_index, end=end_range_index)
        chars.append(current_char)

    number = int(''.join(chars))
    print(number)
    sum = sum + number

print(f'Part 2: {sum}')
