import os

def get_devices(filename: str) -> dict[str, list[str]]:
    devices = dict()
    with open(filename, 'r') as f:
        for line in f.readlines():
            name = line.split(':')[0]
            outputs = line.split(':')[1].strip().split(' ')
            devices[name] = outputs
    return devices

def always(_: list[str]) -> bool:
    return True

def check(steps: list[str], dac_and_fft: bool) -> bool:
    if dac_and_fft:
        return 'dac' in steps and 'fft' in steps
    return True

def count_ways(devices: dict[str, list[str]], step: str, previous: list[str]=[], dac_and_fft: bool=False) -> int:
    nb = 0
    
    # adding current step in previous
    steps = previous.copy()
    steps.append(step)
    
    for next in devices[step]:
        if next == 'out':
            nb += int(check(steps, dac_and_fft))
        else:
            if next in steps:
                # cycling, not going anywhere
                continue
            else:
                nb += count_ways(devices, next, steps, dac_and_fft)

    return nb

def part1(filename: str) -> int:
    devices = get_devices(filename)

    return count_ways(devices, 'you')

def part2(filename: str) -> int:
    devices = get_devices(filename)
    
    nb = 0
    return count_ways(devices, 'svr', dac_and_fft=True)

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day11'))

print("part 1:")
print(part1('sample'))
print(part1('input'))

print("\npart 2:")
print(part2('sample2'))
print(part2('input'))