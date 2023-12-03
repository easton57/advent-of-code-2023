"""
Day 2 part 2
By: Easton Seidel
"""


def main():
    max_values = {}

    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()

    # Find what's possible
    for i in lines:
        hands = i.split(":")[1].split(";")
        game = i.split(":")[0]
        temp_list = [0, 0, 0]  # Red Green Blue

        for j in hands:
            j = j.split(" ")
            j.remove('')
            temp_num = 0

            for k in j:
                try:
                    temp_num = int(k)
                except ValueError:
                    # Not a number!
                    if "blue" in k:
                        if temp_num > temp_list[2]:
                            temp_list[2] = temp_num
                    elif "red" in k:
                        if temp_num > temp_list[0]:
                            temp_list[0] = temp_num
                    else:  # Green
                        if temp_num > temp_list[1]:
                            temp_list[1] = temp_num

        max_values[i] = temp_list

    # Get our value
    total = 0

    for i in max_values:

        total += max_values.get(i)[0] * max_values.get(i)[1] * max_values.get(i)[2]

    # Write the answer out to a file
    with open("day_2_2_output.txt", "w") as o:
        o.write(str(total))


if __name__ == "__main__":
    main()
