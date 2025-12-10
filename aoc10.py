import itertools
import pathlib
import re
from typing import Optional

import numpy as np
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import milp

lines = pathlib.Path('_input/10/input.txt').open('r').readlines()
lines = [line.strip() for line in lines]

lights_list = []
buttons_list = []
joltage_list = []
for line in lines:
    search = re.search(r'\[(.*)] \((.*)\) \{(.*)}', line)
    lights = [char == '#' for char in search.group(1)]
    buttons = [[int(b) for b in bs.strip('()').split(',')] for bs in search.group(2).split(' ')]
    joltage = [int(j) for j in search.group(3).split(',')]
    lights_list.append(lights)
    buttons_list.append(buttons)
    joltage_list.append(joltage)

print(lights_list)
print(buttons_list)


def switch(lights: list[bool], buttons_list: tuple[list[int]]) -> list[bool]:
    new_lights = lights.copy()
    for buttons in buttons_list:
        for button in buttons:
            new_lights[button] = not new_lights[button]
    return new_lights


def find_min_button_switches(lights: list[bool], buttons_list: list[list[int]]) -> int:
    print(f'Target lights: {lights}')
    initial_lights = [False] * len(lights)
    current_num = 1
    while True:
        for subset in itertools.combinations_with_replacement(buttons_list, current_num):
            result = switch(initial_lights, subset)
            if result == lights:
                print(f'Found subset: {subset}')
                return current_num
        current_num += 1
        print(f' Current num: {current_num}')


assert find_min_button_switches([False, True, True, False], [[0, 2], [0, 1], [3], [1, 3]]) == 2


sum = 0
for i in range(len(lights_list)):
    lights = lights_list[i]
    buttons = buttons_list[i]
    minimum = find_min_button_switches(lights, buttons)
    sum += minimum

print(f'Part 1: {sum}')


def switch_joltage(joltage: tuple[int], buttons_list: tuple[list[int]]) -> Optional[tuple[int]]:
    new_joltage = list(joltage)
    for buttons in buttons_list:
        for button in buttons:
            new_joltage[button] -= 1
            if new_joltage[button] < 0:
                return None
    return tuple(new_joltage)



def get_buttons_to_0_at_index(index: int, skip_indexes: set[int], joltage: tuple[int], buttons_list: list[list[int]]):
    buttons_for_index = [buttons for buttons in buttons_list if set(buttons).isdisjoint(skip_indexes) and index in buttons]
    count = joltage[index]
    output = []
    for comb in list(itertools.combinations_with_replacement(buttons_for_index, count)):
        result = switch_joltage(joltage, comb)
        if result is not None:
            output.append(result)
    return output, count


def find_min_switches_joltage(target_joltage: list[int], buttons_list: list[list[int]]) -> int:
    joltages = [(target_joltage, 0)]
    indexes = sorted(range(len(target_joltage)), key=lambda i: target_joltage[i])
    processed_indexes = set()
    for i in indexes:
        new_joltages = []
        for joltage, count in joltages:
            results, new_count = get_buttons_to_0_at_index(i, processed_indexes, tuple(joltage), buttons_list)
            for result in results:
                new_joltages.append((result, count + new_count))
        print(f' {i}: {len(new_joltages)}')
        joltages = new_joltages
        processed_indexes.add(i)
    counts = [c for joltage, c in joltages]
    return min(counts)



def find_min_switches_joltage_ilp(target_joltage: list[int], buttons_list: list[list[int]]) -> int:
    n_buttons = len(buttons_list)
    n_indices = len(target_joltage)

    c = np.ones(n_buttons)

    A = np.zeros((n_indices, n_buttons))
    for i in range(n_indices):
        for b in range(n_buttons):
            if i in buttons_list[b]:
                A[i, b] = 1

    b = np.array(target_joltage)

    integrality = np.ones(n_buttons, dtype=int)
    bounds = Bounds(lb=np.zeros(n_buttons), ub=np.full(n_buttons, np.inf))

    constraint = LinearConstraint(A, b, b)

    res = milp(c=c, constraints=constraint, integrality=integrality, bounds=bounds)

    assert res.success

    return int(res.fun)


print(
    find_min_switches_joltage_ilp(
        [72, 69, 79, 61, 83, 33, 69, 84, 61, 86],
        [
            [1, 4, 5, 9],
            [2, 4, 7],
            [2, 3, 5, 6, 9],
            [0, 1, 2, 3, 8],
            [0, 1, 2, 4, 6, 7, 9],
            [1, 2, 3, 4, 7, 9],
            [4, 9],
            [1, 8],
            [4, 8, 9],
            [0, 1, 3, 6, 7],
            [0, 4, 6, 8],
            [0, 5, 6, 8, 9],
            [0, 2, 3, 7, 8],
        ],
    ),
)


total = 0
for i in range(len(joltage_list)):
    joltage = joltage_list[i]
    print(f'Solving {joltage}')
    buttons = buttons_list[i]
    minimum = find_min_switches_joltage_ilp(joltage, buttons)
    total += minimum

print(f'Part 2: {total}')
