import os
import re

class RangeId:
    def __init__(self, range: str):
        first, last = range.strip().split('-')
        self.first = int(first)
        self.last = int(last)
        
    def __str__(self):
        return f"first: '{self.first}', last: '{self.last}'"
    
    def get_invalid_ids(self) -> list[int]:
        invalid_ids = []
        for i in range(self.first, self.last + 1):
            id = str(i)
            if len(id) % 2 == 0:
                length = int(len(id) / 2)
                if id[:length] == id[length:]:
                    invalid_ids.append(i)
        return invalid_ids
    
    def get_invalid_ids_v2(self) -> list[int]:
        invalid_ids = []
        for i in range(self.first, self.last + 1):
            if RangeId.is_invalid_v2(str(i)):
                invalid_ids.append(i)
        return invalid_ids
    
    def is_invalid_v2(id: str) -> bool:
        length = int(len(id) / 2)
        for l in range(1, length + 1):
            if re.match(f'^({id[:l]})+$', id):
                return True
        return False

def get_ranges(filename: str) -> list[RangeId]:
    ranges = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            for r in line.strip().split(','):
                ranges.append(RangeId(r))
    return ranges

os.chdir('/home/dmorineau/Data/depots/perso/Adventofcode2025/day02')

def sum_invalids(filename: str) -> int:
    sum = 0
    for r in get_ranges(filename):
        for i in r.get_invalid_ids():
            sum += i
    return sum

def sum_invalids_v2(filename: str) -> int:
    sum = 0
    for r in get_ranges(filename):
        for i in r.get_invalid_ids_v2():
            sum += i
    return sum

print("part 1:")
print(sum_invalids('sample'))
print(sum_invalids('input'))

print("\npart 2:")
print(sum_invalids_v2('sample'))
print(sum_invalids_v2('input'))
        