import pathlib

input_str = str(pathlib.Path('/Users/ivana/aoc/2025/5/input.txt').open('r').read()).strip()

ranges_str, inputs_str = input_str.split('\n\n')


ranges = [range.split('-') for range in ranges_str.split('\n')]
ranges = [(int(range_1), int(range_2)) for range_1, range_2 in ranges]
inputs = [int(input_str) for input_str in inputs_str.split('\n')]

fresh_count = 0
for input in inputs:
    for range_start, range_end in ranges:
        if range_start <= input <= range_end:
            fresh_count = fresh_count + 1
            print(input)
            break

print(f'Part 1: {fresh_count}\n')

ranges = sorted(ranges)


def merge_ranges_2(to_merge: list[tuple[int, int]]) -> tuple[bool, list[tuple[int, int]]]:
    merged = False

    to_merge.sort()
    merged_ranges = [to_merge[0]]

    print(f'Ranges count: {len(to_merge)}')

    for i in range(1, len(to_merge)):
        start, end = to_merge[i]
        last_merged_start, last_merged_end = merged_ranges[-1]

        if start <= last_merged_end:
            new_end = max(last_merged_end, end)
            merged_ranges[-1] = last_merged_start, new_end
            merged = True
        else:
            merged_ranges.append((start, end))

    return merged, merged_ranges


while True:
    merged, ranges = merge_ranges_2(ranges)
    if not merged:
        break


fresh_count_2 = 0
for range_start, range_end in ranges:
    count = range_end - range_start + 1
    fresh_count_2 = fresh_count_2 + count

print(f'Part 2: {fresh_count_2}')
