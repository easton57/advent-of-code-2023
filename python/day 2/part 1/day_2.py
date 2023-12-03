"""
Day 2 part 1
By: Easton Seidel
"""


def main():
    possible = []
    impossible = []
    max_values = {'red': 12, 'green': 13, 'blue': 14}

    with open("input.txt") as i:
        lines = i.readlines()

    for i in lines:
        hands = i.split(":")[1].split(";")

        for j in hands:
            j = j.split(" ")
            j.remove('')

            for k in j:
                try:
                    temp_num = int(k)
                except:
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

    with open("day_2_1_output.txt", "w") as o:
        o.write(str(len(possible)))


if __name__ == "__main__":
    main()
