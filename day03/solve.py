import os

def get_banks(filename: str) -> list[str]:
    banks = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            banks.append(line.strip())
    return banks

def get_max_from_subbank(bank: str, start: int, truncate: int) -> int:
    value = max(bank[start:-truncate]) if truncate > 0 else max(bank[start:])
    return int(value), bank[start:].find(str(value)) + start

def get_max_voltage(bank: str, nb_digits: int) -> int:
    voltage = 0
    index = 0
    for n in range(nb_digits):
        value, pos = get_max_from_subbank(bank, index, nb_digits - 1 - n)
        voltage += value * (10 ** (nb_digits - n - 1))
        index = pos + 1
    return voltage

def solve(filename: str, nb_digits: int) -> int:
    voltage = 0
    
    for bank in get_banks(filename):
        voltage += get_max_voltage(bank, nb_digits)
    
    return voltage

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day03'))

print("part 1:")
print(solve('sample', 2))
print(solve('input', 2))

print("part 2:")
print(solve('sample', 12))
print(solve('input', 12))
