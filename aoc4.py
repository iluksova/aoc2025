import pathlib

lines = pathlib.Path('/Users/ivana/aoc/2025/4/input.txt').open('r').readlines()


lines = [line.strip() for line in lines]
input = [list(line) for line in lines]

rows = len(input)
cols = len(input[0])

results = []
offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def round(input: list[list[str]]) -> tuple[list[list[str]], int]:
    count = 0
    output = [[input[j][i] for i in range(cols)] for j in range(rows)]
    for row_i in range(rows):
        for col_i in range(cols):
            if input[row_i][col_i] == '@':
                neighbours_count = 0
                indices = [(row_i + i, col_i + j) for i, j in offsets]
                indices_in_range = [(i, j) for i, j in indices if 0 <= i < rows and 0 <= j < cols]
                for i, j in indices_in_range:
                    if input[i][j] == '@':
                        neighbours_count = neighbours_count + 1
                if neighbours_count < 4:
                    output[row_i][col_i] = 'x'
                    count = count + 1
    return output, count


output, round_count = round(input)
results.append(round_count)
print(f'Part 1: {round_count}')

while round_count > 0:
    output, round_count = round(output)
    print(round_count)
    results.append(round_count)

for line in output:
    print(''.join(line))

print(f'Part 1: {sum(results)}')
