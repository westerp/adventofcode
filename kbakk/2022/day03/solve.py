import pathlib
import string

input_1 = (pathlib.Path(__file__).parent/"input.txt").read_text()

# input_1 = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# """

valmap = {char: val for val, char in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}

totalsum = 0

for line in input_1.splitlines():
    count = len(line)
    comp1, comp2 = line[:count // 2], line[count // 2:]
    for (item,) in set(comp1).intersection(set(comp2)):
        val = valmap[item]
        totalsum+=val
        print(item, val)

print(totalsum)
