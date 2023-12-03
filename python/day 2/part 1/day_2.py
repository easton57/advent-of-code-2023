"""
Day 2 part 1
By: Easton Seidel
"""


def main():
    possible = []
    impossible = []
    max_values = {'Red': 12, 'green': 13, 'blue': 14}

    with open("input.txt") as i:
        lines = i.readlines()

    for i in lines:
        hands = i.split(":")[1].split(";")

        for j in hands:
            j = j.split(" ")




if __name__ == "__main__":
    main()
