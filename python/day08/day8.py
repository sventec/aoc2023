#!/usr/bin/env python3
# https://adventofcode.com/2023/day/8

import math

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read()

ins, rest = lines.split("\n\n")
maps = rest.splitlines()

nodes = {}
for m in maps:
    st, rest = m.split(" = ")
    l, r = rest[1:-1].split(", ")
    nodes[st] = (l, r)

steps = 0
cur = "AAA"
while not cur == "ZZZ":
    for d in ins:
        cur = nodes[cur][0 if d == "L" else 1]
        steps += 1
        if cur == "ZZZ":
            break
print(f"Part 1: {steps}")


steps = 0
path_sts = [n for n in nodes.keys() if n.endswith("A")]
counts = []
for st in path_sts:
    steps = 0
    cur = st
    while not cur.endswith("Z"):
        for d in ins:
            cur = nodes[cur][0 if d == "L" else 1]
            steps += 1
            if cur.endswith("Z"):
                break
    counts.append(steps)
print(f"Part 2: {math.lcm(*counts)}")
