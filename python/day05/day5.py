#!/usr/bin/env python3
# https://adventofcode.com/2023/day/5

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read()

grps = lines.split("\n\n")
seeds = [int(seed) for seed in grps.pop(0).split()[1:]]


def get_locs(seeds):
    l_locs = list(seeds)
    for grp in grps:
        new_locs = {}
        maps = grp.splitlines()[1:]
        # valid_maps = [m for m in maps if set(seeds) & set(range(int((s := m.split())[2])))]
        for m in maps:
            dest, src, l = (int(n) for n in m.split())
            rng = range(src, src + l)
            new_locs.update({loc: dest + rng.index(loc) for loc in l_locs if loc in rng})
        l_locs = [new_locs.get(loc, loc) for loc in l_locs]
    return l_locs


def part_2(grps, seeds):
    seed_ranges = [(s[0], s[1]) for s in zip(seeds[::2], seeds[1::2])]

    max_loc = max([int(m.split()[0]) for m in grps[-1].splitlines()[1:]])
    try:
        from tqdm import tqdm  # Optional progress bar

        iter_range = tqdm(range(max_loc))
    except ImportError:
        iter_range = range(max_loc)

    for i in iter_range:
        i_map = int(i)
        for grp in grps[::-1]:
            for m in grp.splitlines()[1:]:
                dest, src, l = (int(n) for n in m.split())
                rng = range(dest, dest + l)
                if i_map in rng:
                    # print(f"map: {m}")
                    # print(f"{i} in range: {rng}")
                    i_map = src + rng.index(i_map)
                    # print(f"new: {i_map}\n")
                    break
        if any(i_map in range(s[0], s[0] + s[1]) for s in seed_ranges):
            return i
    return -1


print(f"Part 1: {min(get_locs(seeds))}")
print(f"Part 2: {part_2(grps, seeds)}")
