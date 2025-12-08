import pathlib
from collections import Counter

lines = pathlib.Path('_input/7/input.txt').open('r').readlines()
lines = [line.strip() for line in lines]


max_index = len(lines[0])

indices_list = [[index for index, character in enumerate(line) if character == '^'] for line in lines[1:]]

new_lines=[]

split_count=0
beam_start = lines[0].index('S')
beam_position = {beam_start}
path_count = Counter()
path_count[beam_start] = 1
for i, indices in enumerate(indices_list):
    new_beam_position = set()
    if indices:
        beam_splits=set()
        new_path_count = Counter()
        for index in indices:
            for beam in beam_position:
                if index == beam:
                    split_count += 1
                    left_beam = index - 1
                    right_beam = index + 1
                    new_beam_position.add(left_beam)
                    new_beam_position.add(right_beam)

                    new_path_count[left_beam] += path_count[beam]
                    new_path_count[right_beam]+= path_count[beam]

                    beam_splits.add(beam)

        not_changed_beams = beam_position.difference(beam_splits)
        for beam in not_changed_beams:
            new_path_count[beam] += path_count[beam]
        beam_position = new_beam_position.union(not_changed_beams)
        path_count=new_path_count

    new_line=''
    for j, char in enumerate(lines[i+1]):
        if j in beam_position:
            new_line += '|'
        else:
            new_line += char
    new_lines.append(new_line)

for line in new_lines:
    print(line)

print(f'Part 1: {split_count}')
total_paths = sum(path_count.values())
print(f'Part 2: {total_paths}')

