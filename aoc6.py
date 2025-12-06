import pathlib
import re
import math

lines = pathlib.Path('_input/6/input.txt').open('r').readlines()

number_lines = lines[0:-1]
operator_line = lines[-1]


def parse_content(line: str) -> list[str]:
    return re.split(r' +', line.strip())


def sum_of_problems(problems: list[list[int]], operators: list[str]) -> int:
    total = 0
    for index, column in enumerate(problems):
        if operators[index] == '+':
            result = sum(column)
        else:
            result = math.prod(column)
        total += result
    return total


numbers = [parse_content(number_line) for number_line in number_lines]
operators = parse_content(operator_line)

number_columns = [[int(numbers[j][i]) for j in range(len(numbers))] for i in range(len(numbers[0]))]
totat_sum = sum_of_problems(number_columns, operators)
print(f'Part 1: {totat_sum}')

lines = [line.replace('\n', '') for line in lines]
input_transpose = [[lines[j][i] for j in range(len(lines) - 1)] for i in range(len(lines[0]))]
transposed_input = '\n'.join([''.join(row).strip() for row in input_transpose])

transposed_input_numbers = [number_line.split('\n') for number_line in transposed_input.split('\n\n')]
numbers_rows = [[int(number) for number in number_row] for number_row in transposed_input_numbers]

totat_sum_2 = sum_of_problems(numbers_rows, operators)
print(f'Part 2: {totat_sum_2}')
