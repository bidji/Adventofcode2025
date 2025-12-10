import os

def get_positions(filename: str) -> list[list[int]]:
    positions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            position = [int(n) for n in line.strip().split(',')]
            positions.append(position)
    return positions    
        
def area(p1: list[int], p2: list[int]) -> int:
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)

def colored_area(indices: list[list[int]], p1: list[int], p2: list[int]) -> int:
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])
    for y in range(min_y, max_y + 1):
        if len(indices[y]) != 2:
            return 0
        if min_x < indices[y][0] or max_x > indices[y][1]:
            return 0
    return (max_x - min_x + 1) * (max_y - min_y + 1)

def part1(filename: str) -> int:
    positions = get_positions(filename)
    
    max_area = 0
    for n in range(len(positions) - 1):
        for p in positions[n+1:]:
            max_area = max(area(positions[n], p), max_area)
    return max_area
            
os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day09'))

print("part 1:")
print(part1('sample'))
print(part1('input'))