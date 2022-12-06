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

input_iter = iter(input_1.splitlines())

for line1 in input_iter:
    line2 = next(input_iter)
    line3 = next(input_iter)
    print(line1, line2, line3)
    its = set(line1).intersection(line2).intersection(line3).pop()
    val = valmap[its]
    totalsum+=val
    print(its, val)


print(totalsum)
