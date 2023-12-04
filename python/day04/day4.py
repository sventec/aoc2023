#!/usr/bin/env python3
# https://adventofcode.com/2023/day/4

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

# # Uncomment to use sample input, also switch split below
# lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

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
