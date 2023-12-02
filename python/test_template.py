SAMPLE_INPUT = """""".splitlines()

SAMPLE_PART_1 = ""
SAMPLE_PART_2 = ""


def part_1(lines):
    ...


def part_2(lines):
    ...


def main():
    # Test sample input
    try:
        assert part_1(SAMPLE_INPUT) == SAMPLE_PART_1, "1"
        assert part_2(SAMPLE_INPUT) == SAMPLE_PART_2, "2"
    except AssertionError as e:
        print("Test failed on sample:", e)

    # Challenge input part 1
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.read().splitlines()

    print(f"Part 1: {part_1(lines)}")
    print(f"Part 2: {part_2(lines)}")


if __name__ == "__main__":
    main()
