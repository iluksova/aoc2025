import pathlib

with pathlib.Path('/Users/ivana/aoc/2025/2/input.txt').open('r') as f:
    line = f.readlines()[0]


ranges = line.split(',')

def divisor_generator(n):
    for i in range(1, int(n // 2 + 1)):
        if n % i == 0:
            yield i

sum = 0

for range_i in ranges:
    start, end = range_i.split('-', maxsplit=2)

    if len(start) == len(end) and len(start) % 2 == 1:
        continue
    for num in range(int(start), int(end) + 1):
        num_str = str(num)
        num_str_len = len(num_str)

        if (num_str_len % 2) == 0:
            num_str_len_half = int(num_str_len / 2)
            if num_str[0:num_str_len_half] == num_str[num_str_len_half:]:
                sum = sum + num
print(f'Sum (part 1): {sum}')

sum = 0
for range_i in ranges:
    start, end = range_i.split('-', maxsplit=2)

    for num in range(int(start), int(end) + 1):
        num_str = str(num)
        num_str_len = len(num_str)

        for part_length in divisor_generator(num_str_len):
            part_count = num_str_len // part_length
            intervals = [(i * part_length, i * part_length + part_length) for i in range(part_count)]
            parts_are_same = True
            for i in range(1, part_count):
                if num_str[intervals[i][0] : intervals[i][1]] != num_str[intervals[0][0] : intervals[0][1]]:
                    parts_are_same = False
                    break
            if parts_are_same:
                print(num)
                sum = sum + num
                break

print(f'Sum (part2): {sum}')
