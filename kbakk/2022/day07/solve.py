import pathlib
import pprint

input_text = (pathlib.Path(__file__).parent/"input").read_text()

input_example = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

def main(text: str):
    fs = {}
    commands = iter(text.splitlines())
    cwd = []
    last_cmd = ""
    for c in commands:
        if c.startswith("$"):
            last_cmd = c
        # print(last_cmd)
        if c.startswith("$ cd"):
            _, dst = c.split("cd ")
            if dst == "..":
                cwd.pop()
            else:
                cwd.append(dst)
        elif c == "$ ls":
            pass
        # process cmd ouput
        elif last_cmd == "$ ls":
            size_or_type, _name = c.split()
            if size_or_type == "dir":
                continue
            path = ""
            for d in cwd:
                path += f'{d}/'
                fs.setdefault(path, 0)
                fs[path] += int(size_or_type)
    pprint.pprint(fs)
    totalsum = sum(v for v in fs.values() if v <= 100_000)
    print("part 1: at most 100_000 sum:", totalsum)
    print("part 2:")
    tot_space = 70_000_000
    need_space = 30_000_000
    avail_space = tot_space - fs["//"]
    print("available:", avail_space)
    diff_need = need_space-avail_space
    print("diff needs:", diff_need)
    for path, size in sorted(fs.items(), key=lambda i: i[1]):
        if size >= diff_need:
            print(path, size)
            break



print("test")
main(input_example)
print("input")
main(input_text)
