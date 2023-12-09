"""
Day 5 advent of code
by: Easton Seidel
"""
import math


def find_location(target_loc, start, next_name, lines) -> [int, int]:
    loc_int = int(target_loc)
    target = -1
    for j in range(start, len(lines)):
        # Break if we go too far
        if next_name in lines[j]:
            start = j
            return target, start
        elif "map" in lines[j]:
            pass
        elif target == -1:
            # Check the number ranges to see if our seed is there
            nums = lines[j].split(" ")
            map_range = int(nums[2])
            source = int(nums[1])
            destination = int(nums[0])

            if source + map_range - 1 > loc_int > source:
                target = destination + (loc_int - source)
            else:
                start = j

    return target, start


def main():
    # Declare some stuff
    lowest_locations = {}

    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()

    # Read the seeds from the first line and create the max amount of seeds in the dataframe
    seeds = lines[0].split(":")[1].split(" ")[1:]

    # Loop and find our seed locations
    for i in seeds:
        # seed to soil
        i_int = int(i)
        soil, start = find_location(i, 2, "fertilizer", lines)

        # soil to fertilizer
        fertilizer, start = find_location(i, start, "water", lines)

        # fertilizer to water
        water, start = find_location(i, start, "light", lines)

        # water to light
        light, start = find_location(i, start, "temperature", lines)

        # light to temperature
        temperature, start = find_location(i, start, "humidity", lines)

        # temperature to humidity
        humidity, start = find_location(i, start, "location", lines)

        # humidity to location
        location, start = find_location(i, start, "none", lines)

        # Add to our lowest location thing
        lowest_locations[i] = location

    lowest = math.inf
    for i in lowest_locations:
        if -1 < lowest_locations[i] < lowest:
            lowest = lowest_locations[i]

    # Write the answer out to a file
    with open("day_5_output.txt", "w") as o:
        o.write(str(lowest))


if __name__ == "__main__":
    main()
    