import math
import os
import sys

def get_positions(filename: str) -> list[list[int]]:
    positions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            positions.append([int(x) for x in line.strip().split(',')])
    return positions

def euclidean_distance(position1: list[int], position2: list[int]):
    x1, y1, z1 = position1
    x2, y2, z2 = position2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

def find_circuits(circuits: list[set[int]], pair: tuple[int]) -> list[set[int]]:
    founds = []
    for circuit in circuits:
        if pair[0] in circuit or pair[1] in circuit:
            founds.append(circuit)
    return founds

def build_circuits(closest_boxes: list[list[int]]):
    circuits = []
    
    for pair in closest_boxes:
        founds = find_circuits(circuits, pair)
        if len(founds) == 0:
            # no circuit found, creation of a new circuit
            circuits.append(set(pair))
        if len(founds) == 1:
            # 1 circuit found, adding boxes
            founds[0].add(pair[0])
            founds[0].add(pair[1])
        if len(founds) == 2:
            # 2 circuits found, need to merge them
            for box in founds[1]:
                founds[0].add(box)
            circuits.remove(founds[1])
    
    return circuits

def part1(filename: str, nb_iter: int) -> int:
    positions = get_positions(filename)
    
    data = dict()
    for i in range(len(positions[:-1])):
        for j in range(i + 1, len(positions)):
            distance = euclidean_distance(positions[i], positions[j])
            data[distance] = (i, j)
    distances = list(data.keys())
    distances.sort()
    
    closest_boxes = []
    for n in range(nb_iter):
        closest_boxes.append(data[distances[n]])

    circuits = build_circuits(closest_boxes)
        
    lengths = [len(circuit) for circuit in circuits]
    lengths.sort(reverse=True)
    
    length = 1
    for n in range(3):
        length *= lengths[n]
        
    return length
    
os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day08'))

print("part 1:")
print(part1('sample', 10))
print(part1('input', 1000))