#!/usr/bin/env python3
# https://adventofcode.com/2023/day/2
from math import prod

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

games: dict[str, list[dict[str, int]]] = {}
for line in lines:
    draws: list[dict[str, int]] = []
    for draw in line.split(":")[1].split(";"):
        draws.append({(pair := n.split())[1][0]: int(pair[0]) for n in draw.split(",")})
    games[line.split(" ")[1][:-1]] = draws

# # All of above in one line lol
# games = {l.split(" ")[1][:-1]: [{(p := n.split())[1][0]: int(p[0]) for n in d.split(",")} for d in l.split(":")[1].split(";")] for l in lines}

# More readable representation of Part 1
max_each = {}
part_1 = 0
for gid, game in games.items():
    game_max = {}
    for color in ["r", "g", "b"]:
        vals = (draw.get(color, 0) for draw in game)
        game_max[color] = max(vals)
    max_each[gid] = game_max
    if game_max["r"] <= 12 and game_max["g"] <= 13 and game_max["b"] <= 14:
        part_1 += int(gid)

# max_each = {g[0]: {c: max(draw.get(c, 0) for draw in g[1]) for c in ["r", "g", "b"]} for g in games.items()}
# part_1 = sum(int(i) for i, g in max_each.items() if g["r"] <= 12 and g["g"] <= 13 and g["b"] <= 14)

print(f"Part 1: {part_1}")

part_2 = sum(prod(game.values()) for game in max_each.values())
print(f"Part 2: {part_2}")
