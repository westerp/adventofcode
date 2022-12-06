import pathlib

input_1 = (pathlib.Path(__file__).parent/"input.txt").read_text()

# 1 for Rock, 2 for Paper, and 3 for Scissors
score = {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissor
}

beats = {
    "A": "C",
    "B": "A",
    "C": "B"
}
lose = {v: k for k, v in beats.items()}

def to_value(v):
    return score[v]

total_score = 0

# part 2
for row in input_1.splitlines():
    opponent, result = row.split()
    print(row)
    if result == "X":  # lose
        r = to_value(beats[opponent]) + 0
    elif result == "Y":  # draw
        r = to_value(opponent) + 3
    elif result == "Z":  # win
        r = to_value(lose[opponent]) + 6
    else:
        raise ValueError

    print(r)
    total_score += r


print("total:", total_score)
