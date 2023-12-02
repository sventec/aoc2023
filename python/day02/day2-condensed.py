#!/usr/bin/env python3
# https://adventofcode.com/2023/day/2

# --- Day 2 solution condensed into as few lines as possible --- #

from math import prod

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

games = {l.split(" ")[1][:-1]: [{(p := n.split())[1][0]: int(p[0]) for n in d.split(",")} for d in l.split(":")[1].split(";")]for l in lines}
max_each = {g[0]: {c: max(draw.get(c, 0) for draw in g[1]) for c in ["r", "g", "b"]} for g in games.items()}
print(f'Part 1: {sum(int(i) for i, g in max_each.items() if g["r"] <= 12 and g["g"] <= 13 and g["b"] <= 14)}')
print(f"Part 2: {sum(prod(game.values()) for game in max_each.values())}")
