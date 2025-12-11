import pathlib
from collections import Counter
from collections import defaultdict
from collections import deque

lines = pathlib.Path('_input/11/input.txt').open('r').readlines()
lines = [line.strip() for line in lines]


edges : dict[str, set[str]] = defaultdict(set)

degree = Counter()

for line in lines:
    node, rest = line.split(':')
    target_nodes = rest.strip().split(' ')
    edges[node] = set(target_nodes)
    for t in target_nodes:
        degree[t] += 1

sorted_nodes = []
d = deque()
for n in edges:
    if degree[n] == 0:
        d.append(n)
while d:
    n = d.popleft()
    sorted_nodes.append(n)
    targets = edges[n]
    for t in targets:
        degree[t] -=1
        if degree[t] == 0:
            d.append(t)

assert len(sorted_nodes) == len(edges.keys())

def n_paths(start: str, end: str) -> int:
    counts = Counter()
    counts[start] = 1
    for n in sorted_nodes:
        n_count = counts[n]
        for t in edges[n]:
            counts[t] += n_count
    return counts[end]

result = n_paths('you', 'out')

print(f'Part 1: {result}')

n_srv_fft = n_paths('svr', 'fft')
n_fft_dac = n_paths('fft', 'dac')
n_dac_out = n_paths('dac', 'out')

print(f'Part 2: {n_srv_fft*n_fft_dac*n_dac_out}')