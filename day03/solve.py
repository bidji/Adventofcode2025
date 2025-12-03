import os

def get_banks(filename: str) -> list[str]:
    banks = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            banks.append(line.strip())
    return banks

def get_max_voltage(bank: str) -> int:
    maxi = 0
    maxten = int(bank[maxi])
    for i in range(1, len(bank) - 1):
        if maxten < int(bank[i]):
            maxi = i
            maxten = int(bank[i])
    
    maxdigit = int(bank[maxi + 1])
    for j in range(maxi + 1, len(bank)):
        if maxdigit < int(bank[j]):
            maxdigit = int(bank[j])
    
    return maxten * 10 + maxdigit

def solve(filename: str) -> int:
    voltage = 0
    
    for bank in get_banks(filename):
        voltage += get_max_voltage(bank)
    
    return voltage

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day03'))

print("part 1:")
print(solve('sample'))
print(solve('input'))