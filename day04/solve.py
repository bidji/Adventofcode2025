import os

def get_grid(filename: str) -> list[str]:
    grid = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            grid.append(line.strip())
    return grid

def nb_adjacents(grid: list[str], i: int, j: int) -> int:
    nb = 0
    
    for k in range(max(0, i - 1), min(i + 2, len(grid))):
        for l in range(max(0, j - 1), min(j + 2, len(grid[i]))):
            if grid[k][l] == '@':
                nb += 1
    
    return nb - 1

def remove_rolls(grid: list[str]) -> tuple[int, list[str]]:
    new_grid = grid.copy()
    nb = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                continue
            if nb_adjacents(grid, i, j) < 4:
                nb += 1
                new_grid[i] = new_grid[i][:j] + '.' + new_grid[i][j+1:]
    return nb, new_grid
    

def part1(filename: str) -> int:
    grid = get_grid(filename)
    
    nb, _ = remove_rolls(grid)

    return nb

def part2(filename: str) -> int:
    grid = get_grid(filename)
    
    nb, new_grid = remove_rolls(grid)
    total = nb
    while nb > 0:
        nb, new_grid = remove_rolls(new_grid)
        total += nb

    return total

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day04'))

print("part 1:")
print(part1('sample'))
print(part1('input'))

print("part 2:")
print(part2('sample'))
print(part2('input'))