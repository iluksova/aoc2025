import pathlib
import re
import itertools

lines = pathlib.Path('_input/10/input.txt').open('r').readlines()
lines = [line.strip() for line in lines]

lights_list = []
buttons_list = []
joltage_list = []
for line in lines:
    search = re.search(r'\[(.*)] \((.*)\) \{(.*)}', line)
    lights = list(map( lambda char: True if char == '#' else False, search.group(1)))
    buttons = [[int(b) for b  in bs.strip('()').split(',')] for bs in search.group(2).split(' ')]
    joltage =  search.group(3).split(',')
    lights_list.append(lights)
    buttons_list.append(buttons)
    joltage_list.append(joltage)

print(lights_list)
print(buttons_list)

def switch(lights:list[bool], buttons_list: tuple[list[int]]) -> list[bool]:
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

assert find_min_button_switches([False, True, True, False], [[0,2],[0,1],[3],[1,3],]) == 2


sum = 0
for i in range(0, len(lights_list)):
    lights = lights_list[i]
    buttons = buttons_list[i]
    min = find_min_button_switches(lights, buttons)
    sum+=min

print(f'Part 1: {sum}')