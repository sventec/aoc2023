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
        # grp_map = {}
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

        # if set(seeds) & set(range(int(src), int(src) + int(l))):
        #     grp_map = grp_map | {int(src) + i: int(dest) + i for i in range(int(l))}
    # for l_src, l_dest in locs.items():
    #     locs[l_src] = grp_map.get(l_dest) or locs[l_src]

# part_1 = min(locs, key=locs.get)

# print(f"Part 1: {min(locs.values())}")
print(f"Part 1: {min(get_locs(seeds))}")

# BUG: Just runs out of time/memory, modify loc checker function to accept range to check without needing to create entire range in list
seeds_range = []
for i in range(0, len(seeds), 2):
    seeds_range.extend(range(seeds[i], seeds[i] + seeds[i + 1]))

print(f"Part 2: {min(get_locs(seeds_range))}")
