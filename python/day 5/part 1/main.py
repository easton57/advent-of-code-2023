"""
Day 5 advent of code
by: Easton Seidel
"""

import pandas as pd


def main():
    lowest_locations = {}
    
    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()

    # Write the answer out to a file
    with open("day_5_output.txt", "w") as o:
        o.write(str(lowest_locations))


if __name__ == "__main__":
    main()
    