import pathlib

input_str = str(pathlib.Path('_input/12/input.txt').open('r').read()).strip()

input = input_str.split('\n\n')

boards = input[-1].split('\n')
total = 0

for board in boards:
    size_str, counts_str = board.split(':')
    size_x = int(size_str.split('x')[0])
    size_y = int(size_str.split('x')[1])

    counts = [int(count) for count in counts_str.strip().split(' ')]

    if size_x * size_y >= 9 * sum(counts):
        total += 1
print(total)
