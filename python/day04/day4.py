#!/usr/bin/env python3
# https://adventofcode.com/2023/day/4

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

total = 0
card_wins = {}
for i, line in enumerate(lines):
    n = line.split()[2:]

    # # Split for sample input
    # SPLIT_IDX = 5

    # Split for challenge input
    SPLIT_IDX = 10

    n_matches = len(set(n[:SPLIT_IDX]).intersection(set(n[SPLIT_IDX + 1 :])))

    card_wins[line.split()[1][:-1]] = list(range(i + 2, i + n_matches + 2))
    total += int(2 ** (n_matches - 1))

print(f"Part 1: {total}")

num_appear = {}
for i, win in card_wins.items():
    num_appear[i] = num_appear.get(i, 0) + 1
    for w in win:
        num_appear[str(w)] = num_appear.get(str(w), 0) + num_appear.get(i, 1)

print(f"Part 2: {sum(num_appear.values())}")
