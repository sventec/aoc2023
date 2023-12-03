#!/usr/bin/env python3
# https://adventofcode.com/2023/day/3

from collections import OrderedDict, defaultdict
import string

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

# lines = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()

# Transpose for easier x,y access
lines = list(zip(*lines, strict=True))

X_MAX = range(len(lines))
Y_MAX = range(len(lines[0]))
NON_SYMBOL = string.digits + "."
SYMBOL = "*$=/+%#-&@"

# Get location of all symbols
sym = {(x, y) for x in X_MAX for y in Y_MAX if lines[x][y] not in NON_SYMBOL}

# symbols = set()
# for y in Y_MAX:
#     for x in X_MAX:
#         if lines[x][y] not in NON_SYMBOL:
#             print(lines[x][y])
#             symbols.add(lines[x][y])
# print(symbols)

# print(sym)
# print()

# Get location range of all numbers
nums = {}
buf = {}
for y in Y_MAX:
    for x in X_MAX:
        c = lines[x][y]
        if c.isdigit():
            # print(f"{x}, {y}: {c}")
            buf[x] = c
        elif buf:
            idxs = sorted(buf.keys())
            nums[((idxs[0], idxs[-1]), y)] = "".join(buf.values())
            buf = {}
    # New row, clear buf
    buf = {}

# print(nums)

# Keep only numbers adjacent to a symbol
parts = []
for idxs, n in nums.items():
    edges = {(x, idxs[1] + y) for x in range(idxs[0][0] - 1, idxs[0][1] + 2) for y in (-1, 0, 1)}
    if edges.intersection(sym):
        # print("intersection:" + n)
        # print(edges.intersection(sym))
        parts.append(n)
    else:
        print(f"{idxs}: {n}")
    # print(edges)


# print(nums)
# print(parts)

part_1 = sum(int(part) for part in parts)

# 534573 - too low
# 532422
print(f"Part 1: {part_1}")



# print(f"Part 2: {}")
