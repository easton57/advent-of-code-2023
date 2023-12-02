"""
Day one of advent of code in python
"""


def main():
    # read the challenge input
    with open("day_1_input.txt", "r") as f:
        prompt_data = f.read()
    prompt_data = prompt_data.split("\n")

    first_num = None
    second_num = None
    sum = 0

    # doesn't specify if we need to consider numbers spelled out so starting just with integers and a horrible nested for loop
    # Update, it needs the dumb string numbers
    for i in prompt_data:
        line_nums = []
        new_word = ""

        if i != '':
            for j in i:
                # get the nums
                try:
                    int(j)

                    if first_num is None:
                        first_num = j
                    else:
                        second_num = j
                except:
                    # try to construct a word
                    new_word += j

            if second_num is None:
                second_num = first_num

            sum += int(first_num + second_num)

            first_num = None
            second_num = None
    
    with open("day_1_output.txt", "w") as f:
        f.write(str(sum))


def contains_num(string, dict):
    for i in dict:
        if i in string:
            return True, i
    return False, None


if __name__ == "__main__":
    main()

