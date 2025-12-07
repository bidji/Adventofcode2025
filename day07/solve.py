import os

def get_manifold(filename: str) -> list[str]:
    manifold = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            manifold.append(line.strip().replace('S', '|'))
    return manifold

def part1(filename: str):
    manifold = get_manifold(filename)
    width = len(manifold[0])
    
    splits = 0
    for num_line in range(1, len(manifold)):
        for num_col in range(width):
            if manifold[num_line - 1][num_col] == '|':
                # there is a | above
                if manifold[num_line][num_col] == '^':
                    # splitter
                    splits += 1
                    if num_col == 0:
                        manifold[num_line] = '^|' + manifold[num_line][2:]
                    elif num_col == width - 1:
                        manifold[num_line] = manifold[num_line][:-2] + '|^'
                    else:
                        manifold[num_line] = manifold[num_line][:num_col - 1] + '|^|' + manifold[num_line][num_col + 2:]
                else:
                    # no splitter
                    manifold[num_line] = manifold[num_line][:num_col] + '|' + manifold[num_line][num_col + 1:]
    
    return splits
                    

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day07'))

print("part 1:")
print(part1('sample'))
print(part1('input'))

print("part 2:")