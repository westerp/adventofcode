

import pathlib

def detect_so(msg: str, n):
    sopm = []
    for i, s in enumerate(msg, start=1):
        sopm.append(s)
        sopm = sopm[-n:]
        if len(set(sopm)) == n:
            return i
    raise ValueError

def detect_sopm(msg: str):
    return detect_so(msg, 4)

print("tests:")
tests = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
]
for msg, expected, _ in tests:
    print("result:", detect_sopm(msg), "expected:", expected)

input_text = (pathlib.Path(__file__).parent/"input").read_text()
print("part 1:")
print(detect_sopm(input_text))

def detect_som(msg: str):
    return detect_so(msg, 14)

for msg, _, expected in tests:
    print("result:", detect_som(msg), "expected:", expected)

print("part 2:")
print(detect_som(input_text))
