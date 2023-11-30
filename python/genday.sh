#!/bin/bash

# Original script credit: 0xdf
# https://twitter.com/0xdf_

# Usage:
# Set $AOC_SESSION to AOC session cookie: export AOC_SESSION=<cookie>
# Then: source genday.sh <day#>
#  e.g. source genday.sh 3
# Optionally, include the year for completing previous year's challenges:
#       source genday.sh <day#> <year>
#  e.g. source genday.sh 3 2022

day=${1##+(0)}
if ((day < 1 || day > 25)); then
  echo "Provided day is invalid."
  return
fi

project=$(printf "day%02d" "$1")
if [ -z "$AOC_SESSION" ]; then
  echo "\$AOC_SESSION isn't set. Quitting."
  return
fi

year=${2:-$(date +%Y)}
url_base="https://adventofcode.com/${year}/day/${day}"

mkdir "${project}"
cd "${project}" || return

curl -s "${url_base}/input" --cookie "session=${AOC_SESSION}" -o input.txt

echo -n "#!/usr/bin/env python3
# ${url_base}

with open(\"input.txt\", \"r\", encoding=\"utf8\") as f:
    lines = f.read().splitlines()

print(f\"Part 1: {}\")
print(f\"Part 2: {}\")" > day${day}.py
