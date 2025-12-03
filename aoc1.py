import pathlib
from math import trunc


def div(a: int, b: int) -> int:
    return abs(trunc(a / b))


with pathlib.Path('/Users/ivana/aoc/2025/1/input.txt').open('r') as f:
    lines = f.readlines()


current_position = 50
visit_zero = 0
passed_zero_total = 0

for line in lines:
    print(f'{current_position} + {line}')

    steps = int(line[1:])

    if line[0] == 'L':
        steps = -steps
    passed_zero_count = 0

    if -steps >= current_position and current_position != 0:
        passed_zero_count = passed_zero_count + 1

    absolut_position = current_position + steps

    passed_zero_count = passed_zero_count + div(absolut_position, 100)
    print(f' Passed zero {passed_zero_count} times')

    passed_zero_total = passed_zero_total + passed_zero_count

    current_position = absolut_position % 100

    if current_position == 0:
        visit_zero = visit_zero + 1

print(f'Part 1: {visit_zero}')
print(f'Part 2: {passed_zero_total}')
