import os

def get_worksheet_part1(filename: str) -> tuple[list[list[int]], list[str]]:
    values = []
    operators = []
    
    with open(filename, 'r') as f:
        for line in f.readlines():
            data = line.strip().split()
            if data[0] in ['+', '*'] :
                operators = data
            else:
                values.append([int(x) for x in data])
                
    return values, operators

def get_worksheet_part2(filename: str):
    lines = []
    
    with open(filename, 'r') as f:
        for l in f.readlines():
            line = l.replace('\n', '')
            if line.split()[0] in ['+', '*']:
                operators = line.split()
                operators.reverse()
            else:
                lines.append(line)

    values = []
    sub_values = []
    for num_col in range(len(lines[0]) - 1, -1, -1):
        value = ''
        for line in lines:
                value = value + line[num_col].replace(' ', '')
        if value == '':
            # next problem
            values.append(sub_values.copy())
            sub_values.clear()
        else:
            sub_values.append(int(value))
    # add of the last sub_values
    values.append(sub_values.copy())
    
    return values, operators

def add(values: list[list[int]], num_col: int) -> int:
    total = 0
    for num_line in range(len(values)):
        total += values[num_line][num_col]
    return total

def multiply(values: list[list[int]], num_col: int) -> int:
    total = 1
    for num_line in range(len(values)):
        total *= values[num_line][num_col]
    return total

def part1(filename: str):
    values, operators = get_worksheet_part1(filename)
    
    total = 0
    for num_col in range(len(operators)):
        if operators[num_col] == '+':
            total += add(values, num_col)
        else:
            total += multiply(values, num_col)
    
    return total

def part2(filename: str):
    values, operators = get_worksheet_part2(filename)
    
    total = 0
    for num_pb in range(len(operators)):
        if operators[num_pb] == '+':
            sub_total = 0
            for value in values[num_pb]:
                sub_total += value
        else:
            sub_total = 1
            for value in values[num_pb]:
                sub_total *= value
        total += sub_total
        
    return total

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day06'))

print("part 1:")
print(part1('sample'))
print(part1('input'))

print("part 1:")
print(part2('sample'))
print(part2('input'))