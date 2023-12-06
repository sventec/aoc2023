#!/usr/bin/env python3
# https://adventofcode.com/2023/day/6
import math

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

lt, ld = ([int(i) for i in lines[n].split()[1:]] for n in range(2))

# races are tuples of (time, distance)
races = [(t, d) for t, d in zip(lt, ld)]  # noqa: B905
r_times = [(len([t for t in range(r[0]) if (r[0] - t) * t > r[1]])) for r in races]

print(f"Part 1: {math.prod(r_times)}")

time = int("".join(str(n) for n in lt))
distance = int("".join(str(d) for d in ld))

# Quadratic formula, get values at each X (time) intercept -- min & max of winning time range
# Formula for intercepts, transformed from line 12 above. x is t:
# -x^2 + time * x - distance = 0
def q(a, b, c):
    res = []
    d = b * b - 4 * a * c
    s = math.sqrt(abs(d))
    for op in (-1, 1):
        res.append((-b + s * op) / (2 * a))
    return res

ts = q(-1, time, distance * -1)  # [winning time max, winning time min]
print(f"Part 2: {round(ts[0] - ts[1])}")
