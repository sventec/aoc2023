#!/usr/bin/env python3
# https://adventofcode.com/2023/day/3
import string
from collections import defaultdict

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

# Transpose for easier x,y lookup
lines = list(zip(*lines, strict=True))  # type: ignore[arg-type]

X_RANGE = range(len(lines))
Y_RANGE = range(len(lines[0]))
NON_SYMBOL = string.digits + "."

# Get location range of all numbers, e.g. ((0, 2), 0) = 467
nums = {}
buf = {}
for y in Y_RANGE:
    for x in X_RANGE:
        c = lines[x][y]
        if c.isdigit():
            buf[x] = c
        # Add buf to nums: if num in buffer, AND (at end of line OR current char is not digit)
        if buf and (x == X_RANGE[-1] or not c.isdigit()):
            nums[(((k := list(buf.keys()))[0], k[-1]), y)] = "".join(buf.values())
            buf = {}

# Get location of all symbols
sym = {(x, y) for x in X_RANGE for y in Y_RANGE if lines[x][y] not in NON_SYMBOL}

# Keep only numbers adjacent to a symbol
parts = defaultdict(list)
for idxs, n in nums.items():
    edges = {(x, idxs[1] + y) for x in range(idxs[0][0] - 1, idxs[0][1] + 2) for y in (-1, 0, 1)}
    for s in edges.intersection(sym):
        parts[s].append(int(n))
    # else:
    #     # Display number context (edges), only displays invalid numbers
    #     print(f"{idxs}: {n}")
    #     for y in (-1, 0, 1):
    #         for x in range(idxs[0][0] -1, idxs[0][1] + 2):
    #             try:
    #                 print(lines[x][idxs[1] + y], end="")
    #             except IndexError:
    #                 print("x", end="")
    #         print()

part_1 = sum(sum(part) for part in parts.values())
print(f"Part 1: {part_1}")

part_2 = sum(nums[0] * nums[1] for s, nums in parts.items() if lines[s[0]][s[1]] == "*" and len(nums) == 2)
print(f"Part 2: {part_2}")
