import os

class Range:
    def __init__(self, range: str):
        self.start = int(range.split('-')[0])
        self.end = int(range.split('-')[1])
    
    def __str__(self):
        return f"{self.start} - {self.end}"
    
    def contains(self, id):
        return self.start <= id and id <= self.end
    
    def length(self):
        if self.end < self.start:
            return 0
        return self.end - self.start + 1

def get_ranges_and_ingredients(filename: str) -> tuple[list[Range], list[int]]:
    ranges = []
    ingredients = []
    
    with open(filename, 'r') as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                # blank line, skip
                continue
            if '-' in line:
                # it's a range
                ranges.append(Range(line.strip()))
            else:
                # it's an ingredient
                ingredients.append(int(line.strip()))
    
    return ranges, ingredients

def is_fresh(ingredient: int, ranges: list[Range]):
    for r in ranges:
        if r.contains(ingredient):
            return True
        if r.start > ingredient:
            return False
    return False

def part1(filename: str):
    ranges, ingredients = get_ranges_and_ingredients(filename)
    ranges.sort(key=lambda r: r.start)
    
    nb = 0
    for ingredient in ingredients:
        if is_fresh(ingredient, ranges):
            nb += 1
            
    return nb

def part2(filename: str):
    ranges, _ = get_ranges_and_ingredients(filename)
    ranges.sort(key=lambda r: r.start)
    
    for i in range(len(ranges) - 1):
        for j in range(i+1, len(ranges)):
            if ranges[j].start <= ranges[i].end:
                ranges[j].start = ranges[i].end + 1
    
    nb = 0
    for r in ranges:
        nb += r.length()
        
    return nb
        

os.chdir(os.path.expanduser('~/Data/depots/perso/Adventofcode2025/day05'))

print("part 1")
print(part1('sample'))
print(part1('input'))

print("part 2")
print(part2('sample'))
print(part2('input'))