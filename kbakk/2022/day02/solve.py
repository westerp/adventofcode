import pathlib

input_1 = (pathlib.Path(__file__).parent/"input.txt").read_text()

# 1 for Rock, 2 for Paper, and 3 for Scissors
score = {
    1: ["A", "X"], # rock
    2: ["B", "Y"], # paper
    3: ["C", "Z"], # scissor
}
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def to_value(v):
    for key, val_list in score.items():
        if v in val_list:
            return key
    raise ValueError

total_score = 0

# part 1
for row in input_1.splitlines():
    opponent, me = row.split()
    op_v = to_value(opponent)
    me_v = to_value(me)
    total_score += me_v
    if op_v == me_v:
        total_score += 3
    elif (me_v == 2 and op_v == 1) \
        or (me_v == 3 and op_v == 2) \
        or (me_v == 1 and op_v == 3):
        total_score+=6
    else:
        total_score += 0

print(total_score)
