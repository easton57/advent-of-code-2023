"""
Day one of advent of code in python
"""


def main():
    # read the challenge input
    with open("day_1_2_input.txt", "r") as f:
        prompt_data = f.read()
    prompt_data = prompt_data.split("\n")

    num_dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7',
                "eight": '8', "nine": '9'}
    final_nums = []
    sum = 0

    for i in prompt_data:
        line_nums = []
        new_word = ""

        if i != '':
            for j in i:
                # get the nums
                try:
                    int(j)

                    # append the number
                    line_nums.append(j)
                    new_word = ""
                except:
                    # try to construct a word
                    new_word += j

                # Check the word
                if new_word in num_dict:
                    int(num_dict.get(new_word))

                    # append the num
                    line_nums.append(str(num_dict.get(new_word)))
                    new_word = ""

                # Check to see if a key is contained in the string
                contained, returned_num = contains_num(new_word, num_dict)

                if contained:
                    line_nums.append(str(num_dict.get(returned_num)))
                    new_word = ""

            reverse_str = ""
            reverse_num = []

            # Check the string backwards
            for j in reversed(i):
                # get the nums
                try:
                    int(j)

                    # append the number
                    reverse_num = [j] + reverse_num
                    reverse_str = ""
                except:
                    # try to construct a word
                    reverse_str = j + reverse_str

                # Check the word
                if reverse_str in num_dict:
                    int(num_dict.get(reverse_str))

                    # append the num
                    reverse_num = [str(num_dict.get(reverse_str))] + reverse_num
                    reverse_str = ""

                # Check to see if a key is contained in the string
                contained, returned_num = contains_num(reverse_str, num_dict)

                if contained:
                    reverse_num = [str(num_dict.get(returned_num))] + reverse_num
                    reverse_str = ""

            if reverse_num[-1] != line_nums[-1] and reverse_num[-1] is not None:
                sum += int(line_nums[0] + reverse_num[-1])
                final_nums.append(int(line_nums[0] + reverse_num[-1]))
            else:
                sum += int(line_nums[0] + line_nums[-1])
                final_nums.append(int(line_nums[0] + line_nums[-1]))

    with open("day_1_2_output.txt", "w") as f:
        f.write(str(sum))


def contains_num(string, dict):
    for i in dict:
        if i in string:
            return True, i
    return False, None


if __name__ == "__main__":
    main()

