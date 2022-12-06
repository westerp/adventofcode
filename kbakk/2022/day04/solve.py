import pathlib

input_text = (pathlib.Path(__file__).parent/"input").read_text()

input_text_ex = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def to_range(v):
    start, end = v.split("-")
    return range(int(start), int(end)+1)

total_p1 = 0
total_p2 = 0

for pairs in input_text.splitlines():
    e1, e2 = pairs.split(",")
    e1set, e2set = set(to_range(e1)), set(to_range(e2))
    if e1set.issubset(e2set) or e2set.issubset(e1set):
        print(pairs, "issubset")
        total_p1 +=1
    if e1set.intersection(e2set) or e2set.intersection(e1set):
        print(pairs, "intersection")
        total_p2+=1
print("part 1:", total_p1)
print("part 2:", total_p2)
