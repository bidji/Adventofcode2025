import os

def get_manifold(filename: str) -> list[list[str]]:
    manifold = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            manifold.append([c for c in line.strip().replace('S', '1')])
    return manifold

def part1(filename: str):
    manifold = get_manifold(filename)
    width = len(manifold[0])
    
    splits = 0
    for num_line in range(1, len(manifold)):
        for num_col in range(width):
            if manifold[num_line - 1][num_col] == '1':
                # there is a beam above
                if manifold[num_line][num_col] == '^':
                    # splitter
                    splits += 1
                    if num_col > 0:
                        manifold[num_line][num_col - 1] = '1'
                    if num_col < width - 1:
                        manifold[num_line][num_col + 1] = '1'
                else:
                    # no splitter
                    manifold[num_line][num_col] = '1'
    
    return splits

def part2(filename: str):
    manifold = get_manifold(filename)
    width = len(manifold[0])
    
    for num_line in range(1, len(manifold)):
        for num_col in range(width):
            if manifold[num_line - 1][num_col] != '.' and manifold[num_line - 1][num_col] != '^':
                # there is a beam above
                beam_size = int(manifold[num_line - 1][num_col])
                if manifold[num_line][num_col] == '^':
                    # splitter
                    if num_col > 0:
                        existing_beam = int(manifold[num_line][num_col - 1].replace('.', '0'))
                        manifold[num_line][num_col - 1] = str(beam_size + existing_beam)
                    if num_col < width - 1:
                        existing_beam = int(manifold[num_line][num_col + 1].replace('.', '0'))
                        manifold[num_line][num_col + 1] = str(beam_size + existing_beam)
                else:
                    # no splitter
                    existing_beam = int(manifold[num_line][num_col].replace('.', '0'))
                    manifold[num_line][num_col] = str(beam_size + existing_beam)

    nb_beams = 0            
    for c in manifold[-1]:
        if c != '.' and c != '^':
            nb_beams += int(c)
    
    return nb_beams

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day07'))

print("part 1:")
print(part1('sample'))
print(part1('input'))

print("part 2:")
print(part2('sample'))
print(part2('input'))