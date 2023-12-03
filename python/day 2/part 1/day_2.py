"""
Day 2 part 1
By: Easton Seidel
"""


def main():
    possible = []
    impossible = []
    max_values = {'red': 12, 'green': 13, 'blue': 14}

    # Read our input
    with open("input.txt") as i:
        lines = i.readlines()

    # Find what's possible
    for i in lines:
        hands = i.split(":")[1].split(";")

        for j in hands:
            if i in impossible:
                break

            temp_num = 0
            j = j.split(" ")
            j.remove('')

            for k in j:
                try:
                    temp_num = int(k)
                except ValueError:
                    # Not a number!
                    if "blue" in k:
                        if temp_num > max_values.get("blue"):
                            impossible.append(i)
                            break
                    elif "red" in k:
                        if temp_num > max_values.get("red"):
                            impossible.append(i)
                            break
                    else:  # Green
                        if temp_num > max_values.get("green"):
                            impossible.append(i)
                            break

        if i not in impossible:
            possible.append(i)

    # Get our value
    total = 0

    for i in possible:
        i = i.split(":")[0].split(" ")

        total += int(i[1])

    # Write the answer out to a file
    with open("day_2_1_output.txt", "w") as o:
        o.write(str(total))


if __name__ == "__main__":
    main()
