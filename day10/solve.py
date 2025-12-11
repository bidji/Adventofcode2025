import numpy as np
import os
import re
from itertools import product

def get_machines(filename: str):
    machines = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            lights = [1 if l == '#' else 0 for l in re.findall('([.#]+)', line)[0]]
            
            data = re.findall('\(([0-9,]+)\)', line)
            buttons = [[0] * len(data) for _ in range(len(lights))]
            for j, indices in enumerate(data):
                for i in indices.split(','):
                    buttons[int(i)][j] = 1
                
            joltage = [int(j) for j in re.findall('{([0-9,]+)}', line)[0].split(',')]
            
            machines.append({'lights': lights, 'buttons': buttons, 'joltage': joltage})
    return machines

def find_all_solutions(lights, buttons):
    solutions = []
    A = np.array(buttons, dtype=int)
    b = np.array(lights, dtype=int)
    
    for candidate in product([0, 1], repeat=len(buttons[0])):
        solution_vector = np.array(candidate)
        result = np.dot(A, solution_vector) % 2
        
        if np.array_equal(result, b):
            solutions.append([p for p in candidate])
    
    return solutions
            
def part1(filename: str) -> int:
    machines = get_machines(filename)
    
    sum_press = 0
    for machine in machines:
        solutions = find_all_solutions(machine['lights'], machine['buttons'])
        
        if len(solutions) > 0:
            sum_press += min([sum(s) for s in solutions])
    
    return sum_press

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day10'))

print("part 1:")
print(part1("sample"))
print(part1("input"))
