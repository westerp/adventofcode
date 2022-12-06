import pathlib

input_1 = (pathlib.Path(__file__).parent/"input.txt").read_text()

elfs_sums = {}

for elf, segment in enumerate(input_1.split("\n\n"), start=1):
    elf_sum = sum(int(i) for i in segment.split())
    elfs_sums[elf] = elf_sum

print("part 1", *sorted(elfs_sums.items(), key=lambda i: i[1]), sep="\n")
top_3 = list(sorted(elfs_sums.items(), key=lambda i: i[1], reverse=True))[:3]
print("part 2", top_3, sum(i[1] for i in top_3))
