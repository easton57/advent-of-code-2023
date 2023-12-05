"""
Day 3 advent of code
by: Easton Seidel
"""

sum = 0
lines = None
line_blacklist = []


def main():
    global sum
    global lines
    global line_blacklist
    int_strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()

    # Loop through the range of the lines
    for i in range(len(lines)):
        # Pull current line stats
        print(f"\nCurrent working line: {lines[i]}")
        curr_line_nums = find_indexes(lines[i], int_strings)
        curr_line_chars = find_indexes(lines[i], int_strings, True)

        # Find out if we're on the first line, last line, or somewhere inbetween
        if i == 0:  # First Line
            next_line_chars = find_indexes(lines[i + 1], int_strings, True)

            # Check to see if any are close
            for j in curr_line_nums:
                # current line
                check_valid_num(curr_line_chars, curr_line_nums, j, lines, i)

                # next line
                check_valid_num(next_line_chars, curr_line_nums, j, lines, i)

        elif i == len(lines) - 1:  # Last Line
            prev_line_chars = find_indexes(lines[i - 1], int_strings, True)

            # Check to see if any are close
            for j in curr_line_nums:
                # current line
                check_valid_num(curr_line_chars, curr_line_nums, j, lines, i)

                # prev line
                check_valid_num(prev_line_chars, curr_line_nums, j, lines, i)

        else:  # Everything else
            next_line_chars = find_indexes(lines[i + 1], int_strings, True)
            prev_line_chars = find_indexes(lines[i - 1], int_strings, True)

            # Check to see if any are close
            for j in curr_line_nums:
                # current line
                check_valid_num(curr_line_chars, curr_line_nums, j, lines, i)

                # next line
                check_valid_num(next_line_chars, curr_line_nums, j, lines, i)

                # prev line
                check_valid_num(prev_line_chars, curr_line_nums, j, lines, i)

    # Write the answer out to a file
    with open("day_3_output.txt", "w") as o:
        print(f"\nFinal sum: {sum}")
        o.write(str(sum))


def check_valid_num(line_chars, line_nums, num, lines, i) -> None:
    """ Checks a found number to the listed simbols to validate them """
    global sum
    global line_blacklist

    num_2 = num + 1  # i with a plus 1
    num_3 = num - 1  # i with a minus 1

    if num in line_chars or num_2 in line_chars or num_3 in line_chars:
        s, e = construct_num(line_nums, num)
        new_num = lines[i][s:e]

        try:
            # Add the number to the sum
            sum += int(new_num)

            # remove the number from the line string
            lines[i] = lines[i].split(new_num, 1)

            # Create a solid string again
            fill = "." * len(new_num)
            lines[i] = fill.join(lines[i])

            print(f"Number used: {new_num} and new sum: {sum}")
        except ValueError:
            print("Number previously accounted for... continuing...")


def find_indexes(search_list, target, avoid=False) -> list:
    """
    Function to find all instances of characters that aren't a period.
    Returns a list of indexes.
    target should be a list or single value of the same type
    """
    indexes = []

    if not avoid:
        for i in range(len(search_list)):
            if search_list[i] in target:
                indexes.append(i)
    else:
        for i in range(len(search_list)):
            if search_list[i] not in [".", "\n"] and not search_list[i] in target:
                indexes.append(i)

    return indexes


def construct_num(idxs, hit_idx) -> [int, int]:
    """ Used to bring our indexes back together to pull a number """
    starting_num = 0
    ending_num = 0

    # find out what direction we need to go to create the slice
    start = idxs.index(hit_idx)

    if idxs[start + 1] == hit_idx + 1 and hit_idx - 1 == idxs[start - 1]:
        starting_num = hit_idx - 1
        ending_num = hit_idx + 1
    elif idxs[start + 1] > hit_idx + 1:
        ending_num = hit_idx

        # check for third num behind the second
        if start - 2 < len(idxs) and idxs[start - 2] == hit_idx - 2:
            starting_num = hit_idx - 2
        else:
            starting_num = hit_idx - 1
    elif idxs[start - 1] < hit_idx - 1:
        starting_num = hit_idx

        # check for third num behind the second
        if start + 2 < len(idxs) and idxs[start + 2] == hit_idx + 2:
            ending_num = hit_idx + 2
        else:
            ending_num = hit_idx + 1

    return starting_num, ending_num + 1


if __name__ == "__main__":
    main()
