import pathlib
import numpy as np
from scipy.spatial import distance_matrix

lines = pathlib.Path('_input/8/input.txt').open('r').readlines()
lines = [line.strip() for line in lines]

coordinates =  np.array([line.strip().split(',') for line in lines], dtype=int)

distances = distance_matrix(coordinates, coordinates)

distances_map = {}
for i in range(distances.shape[0]):
    for j in range(distances.shape[1]):
        if i<j:
            distances_map[(i, j)] = distances[i, j]

sorted_distances = {k: v for k, v in sorted(distances_map.items(), key=lambda item: item[1])}

i=0
cycles=[]
for junction, distance in sorted_distances.items():
    print(f'{junction} : {distance}')
    if i < 1000:
        added = False
        added_c = []
        for c in cycles:
            if junction[0] in c or junction[1] in c:
                c.add(junction[0])
                c.add(junction[1])
                added = True
                added_c.append(c)
        if len(added_c) == 0:
            cycles.append({junction[0], junction[1]})
        elif len(added_c) > 1:
            union_c = set()
            for c in added_c:
                cycles.remove(c)
                union_c = union_c.union(c)
            cycles.append(union_c)
        i+=1
    else:
        break

print(cycles)
sizes = sorted([len(c) for c in cycles], reverse=True)
print(sizes)

sum = 1
for i in range(3):
    sum = sizes[i] * sum

print(f'Part 1: {sum}')

n = len(coordinates) -1
print(n)


cycles=[]
last = None
for junction, distance in sorted_distances.items():
    if len(set().union(*cycles)) == 999:
        last = junction

    added = False
    added_c = []
    for c in cycles:
        if junction[0] in c or junction[1] in c:
            c.add(junction[0])
            c.add(junction[1])
            added = True
            added_c.append(c)
    if len(added_c) == 0:
        cycles.append({junction[0], junction[1]})
    elif len(added_c) > 1:
        union_c = set()
        for c in added_c:
            cycles.remove(c)
            union_c = union_c.union(c)
        cycles.append(union_c)

sum_2 = coordinates[last[0]][0] * coordinates[last[1]][0]
print(f'Part 2: {sum_2}')

