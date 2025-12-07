import os

def get_rotations(filename: str):
    with open(filename, 'r') as f:
        return [r.strip() for r in f.readlines()]

def rotate(starting: int, rotation: str) -> int:
    modifier = int(rotation.replace("L", "-").replace("R",""))
    value = starting + modifier
    z = 0
    if modifier < 0 and value < 1:
        # negative modifier and value reached at least 0
        z = int(value * -1 / 100)
        if starting != 0:
            # we pass through 0 going to negative value
            z += 1
    if modifier > 0 and value > 99:
        # positive modifier and value reached at least 100 (which means 0)
        z = int(value / 100)
    return value % 100, z

def part1(filename: str) -> int:
    nb = 0
    value = 50
    for rotation in get_rotations(filename):
        value, _ = rotate(value, rotation)
        if value == 0:
            nb += 1
    return nb

def part2(filename: str) -> int:
    nb = 0
    value = 50
    for rotation in get_rotations(filename):
        value, z = rotate(value, rotation)
        nb += z
    return nb

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day01'))

print("part 1:")
print(f"sample: {part1('sample')}")
print(f"input: {part1('input')}")

print("\npart 2:")
print(f"sample: {part2('sample')}")
print(f"input: {part2('input')}")