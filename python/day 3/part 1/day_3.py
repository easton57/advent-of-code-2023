"""
Day 3 advent of code
by: Easton Seidel
"""


def main():
    int_strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    sum = 0

    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()

    # Loop through the range of the lines
    for i in range(len(lines)):
        # Pull current line stats
        curr_line_nums = find_indexes(lines[i], int_strings)
        curr_line_chars = find_indexes(lines[i], int_strings, True)
        line_blacklist = []

        # Find out if we're on the first line, last line, or somewhere inbetween
        if i == 0:  # First Line
            next_line_chars = find_indexes(lines[i + 1], int_strings, True)

            # Check to see if any are close
            for j in curr_line_nums:
                j_2 = j + 1  # i with a plus 1
                j_3 = j - 1  # i with a minus 1

                # current line
                if j in curr_line_chars or j_2 in curr_line_chars or j_3 in curr_line_chars:
                    s, e = construct_num(curr_line_nums, j)

                    # Get the number that's good and add it to the sum
                    if lines[i][s:e] not in line_blacklist:
                        sum += int(lines[i][s:e])
                        line_blacklist.append(lines[i][s:e])

                # next line
                if j in next_line_chars or j_2 in next_line_chars or j_3 in next_line_chars:
                    s, e = construct_num(curr_line_nums, j)

                    # Get the number that's good and add it to the sum
                    if lines[i][s:e] not in line_blacklist:
                        sum += int(lines[i][s:e])
                        line_blacklist.append(lines[i][s:e])

        elif i == len(lines) - 1:  # Last Line
            prev_line_chars = find_indexes(lines[i - 1], int_strings, True)

            # Check to see if any are close
            for j in curr_line_nums:
                j_2 = j + 1  # i with a plus 1
                j_3 = j - 1  # i with a minus 1

                # current line
                if j in curr_line_chars or j_2 in curr_line_chars or j_3 in curr_line_chars:
                    s, e = construct_num(curr_line_nums, j)

                    # Get the number that's good and add it to the sum
                    if lines[i][s:e] not in line_blacklist:
                        sum += int(lines[i][s:e])
                        line_blacklist.append(lines[i][s:e])

                # prev line
                if j in prev_line_chars or j_2 in prev_line_chars or j_3 in prev_line_chars:
                    s, e = construct_num(curr_line_nums, j)

                    # Get the number that's good and add it to the sum
                    if lines[i][s:e] not in line_blacklist:
                        sum += int(lines[i][s:e])
                        line_blacklist.append(lines[i][s:e])

        else:  # Everything else
            next_line_chars = find_indexes(lines[i + 1], int_strings, True)
            prev_line_chars = find_indexes(lines[i - 1], int_strings, True)

            # Check to see if any are close
            for j in curr_line_nums:
                j_2 = j + 1  # i with a plus 1
                j_3 = j - 1  # i with a minus 1

                # current line
                if j in curr_line_chars or j_2 in curr_line_chars or j_3 in curr_line_chars:
                    s, e = construct_num(curr_line_nums, j)

                    # Get the number that's good and add it to the sum
                    if lines[i][s:e] not in line_blacklist:
                        sum += int(lines[i][s:e])
                        line_blacklist.append(lines[i][s:e])

                # next line
                if j in next_line_chars or j_2 in next_line_chars or j_3 in next_line_chars:
                    s, e = construct_num(curr_line_nums, j)

                    # Get the number that's good and add it to the sum
                    if lines[i][s:e] not in line_blacklist:
                        sum += int(lines[i][s:e])
                        line_blacklist.append(lines[i][s:e])

                # prev line
                if j in prev_line_chars or j_2 in prev_line_chars or j_3 in prev_line_chars:
                    s, e = construct_num(curr_line_nums, j)

                    # Get the number that's good and add it to the sum
                    if lines[i][s:e] not in line_blacklist:
                        sum += int(lines[i][s:e])
                        line_blacklist.append(lines[i][s:e])

    # Write the answer out to a file
    with open("day_3_output.txt", "w") as o:
        o.write(str(sum))


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
        if idxs[start - 2] == hit_idx - 2:
            starting_num = hit_idx - 2
        else:
            starting_num = hit_idx - 1
    elif idxs[start - 1] < hit_idx - 1:
        starting_num = hit_idx

        # check for third num behind the second
        if hit_idx and idxs[start + 2] == hit_idx + 2:
            ending_num = hit_idx + 2
        else:
            ending_num = hit_idx + 1

    return starting_num, ending_num + 1


if __name__ == "__main__":
    main()
