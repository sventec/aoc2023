#!/usr/bin/env python3
# https://adventofcode.com/2023/day/1

import re

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

vals = [[c for c in l if c.isdigit()] for l in lines]
cals = [int(v[0] + v[-1]) for v in vals]
print(f"Part 1: {sum(cals)}")

# lines = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".splitlines()

# The sample output above produces the correct answer

n_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

lines = [re.sub(f"({'|'.join(n_map.keys())})", lambda n: str(n_map[n.group()]), l) for l in lines]

vals = [[c for c in l if c.isdigit()] for l in lines]
cals = [int(v[0] + v[-1]) for v in vals]
# cals = [int(v[0] + v[-1]) if len(v) > 1 else int(v[0]) for v in vals]

# BUG: This isn't giving the correct result, need to track down the issue

# wrong:
# 56322
# 53262
# 55108 (part 1)
print(f"Part 2: {sum(cals)}")
