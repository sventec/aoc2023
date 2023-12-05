#!/usr/bin/env python3
# https://adventofcode.com/2023/day/5

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read()


# lines = """seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4"""

grps = lines.split("\n\n")
seeds = [int(seed) for seed in grps.pop(0).split()[1:]]


def get_locs(seeds):
    # locs = {s: s for s in seeds}
    l_locs = list(seeds)
    for grp in grps:
        new_locs = {}
        maps = grp.splitlines()[1:]
        # valid_maps = [m for m in maps if set(seeds) & set(range(int((s := m.split())[2])))]
        for m in maps:
            dest, src, l = (int(n) for n in m.split())
            rng = range(src, src + l)  # + 1?
            # FIXME: ew?
            for i, loc in enumerate(l_locs):
                if loc in rng:
                    # l_locs[i] = dest + rng.index(loc)
                    new_locs[loc] = dest + rng.index(loc)
        # FIXME: no reason to iterate over locs twice
        for i, loc in enumerate(l_locs):
            if loc in new_locs.keys():
                l_locs[i] = new_locs[loc]
    return l_locs


print(f"Part 1: {min(get_locs(seeds))}")


def part_2(grps, seeds):
    seed_ranges = [(s[0], s[1]) for s in zip(seeds[::2], seeds[1::2], strict=True)]

    loc_grps = grps[-1]
    max_loc = max([int(m.split()[0]) for m in loc_grps.splitlines()[1:]])

    try:
        from tqdm import tqdm

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


print(f"Part 2: {part_2(grps, seeds)}")
