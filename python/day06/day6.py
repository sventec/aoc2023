#!/usr/bin/env python3
# https://adventofcode.com/2023/day/6
import math

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

lt, ld = ([int(i) for i in lines[n].split()[1:]] for n in range(2))
races = [(t, d) for t, d in zip(lt, ld)]  # noqa: B905

# Brute force solve method (works fine)
# r_times = [(len([t for t in range(r[0]) if (r[0] - t) * t > r[1]])) for r in races]
# print(f"Part 1: {math.prod(r_times)}")

# Quadratic formula, get values at each X (time) intercept -- min & max of winning time range
# Formula for intercepts, transformed from line 12 above. x is t:
# -x^2 + time * x - distance = 0
def q(b, c):
    # 'a' of formula is always -1, has been simplified out
    res = []
    d = b * b + 4 * c
    s = math.sqrt(abs(d))
    for op in (-1, 1):
        root = (-b + s * op) / -2
        if int(root) == root:
            # Perfect square (tie), offset 1
            root += op
        res.append(root)
    # [winning time max, winning time min]
    return math.floor(res[0]) - math.ceil(res[1]) + 1

r_times = [q(t, d * -1) for t, d in races]
print(f"Part 1: {math.prod(r_times)}")

time = int("".join(str(n) for n in lt))
distance = int("".join(str(d) for d in ld))

ts = q(time, distance * -1)
print(f"Part 2: {ts}")
