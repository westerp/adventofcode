import pathlib
import re

input_text = (pathlib.Path(__file__).parent/"input").read_text()

input_text_ex ="""\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def is_letter(c):
    return 65 <= ord(c) <= 90

def parse_stacks(in_: str):
    # get stacks first
    parsed = [l for l in
        in_.splitlines()
        if "[" in l]
    parsed = list(reversed(parsed))
    # get positions based on bottom stack
    stacks = {pos: [] for pos, c in enumerate(parsed[0]) if is_letter(c)}
    for line in parsed:
        for pos in stacks:
            try:
                val = line[pos]
                if val.strip():
                    stacks[pos].append(val)
            except (KeyError, IndexError) as e:
                pass #print(e, line, pos)
    # new stack with names matching puzzle
    return {i: stacks[key] for i, key in enumerate(stacks, start=1)}

def parse_instructions(in_: str):
    # parse into tuple pairs:
    # count, source stack, target stack
    instructions = []
    for line in in_.splitlines():
        regex = r"move (\d+) from (\d+) to (\d+)"
        matches = re.match(regex, line)
        if matches:
            instructions.append((int(matches.group(1)), int(matches.group(2)), int(matches.group(3))))
    return instructions

def stack_organizer(move_multiple=False):
    stacks = parse_stacks(input_text)
    instructions = parse_instructions(input_text)

    def poplastn(pop: int, l: list):
        popped, l = l[-pop:], l[:-pop]
        return popped, l

    print("before", stacks)
    for count, stack_src, stack_tgt in instructions:
        items, stacks[stack_src] = poplastn(count, stacks[stack_src])
        print(f"moving {count} items ({items}) from {stack_src} to {stack_tgt}")
        if not move_multiple:
            items = reversed(items)
        stacks[stack_tgt].extend(items)
        print("after", stacks)

    # result
    for k, v in stacks.items():
        print(v[-1], end="")
    print()

print("part1:")
stack_organizer()
print("part2:")
stack_organizer(True)
