"""
Day one of advent of code in python
"""


def main():
    # read the challenge input
    with open("day_1_input.txt", "r") as f:
        prompt_data = f.read()
    prompt_data = prompt_data.split("\n")

    num_dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    expanded_dict = {}
    final_nums = []
    sum = 0

    # Get all permutations
    for i in num_dict:
        for j in num_dict:
            expanded_dict[i + j] = num_dict.get(i) + num_dict.get(j)

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

                    # append the number
                    line_nums.append(j)
                    new_word = ""
                except:
                    # try to construct a word
                    new_word += j

                # Check the word
                # if new_word in total_dict:
                #     int(total_dict.get(new_word))

                #     # append the num
                #     line_nums.append(str(total_dict.get(new_word)))
                #     new_word = ""

                # Check to see if a key is contained in the string
                contained, returned_num = contains_num(new_word, expanded_dict)

                if contained:
                    line_nums.append(str(expanded_dict.get(returned_num)))
                    new_word = ""

            sum += int(line_nums[0] + line_nums[-1])
            final_nums.append(int(line_nums[0] + line_nums[-1]))
    
    with open("day_1_output.txt", "w") as f:
        f.write(str(sum))


def contains_num(string, dict):
    for i in dict:
        if i in string:
            return True, i
    return False, None


if __name__ == "__main__":
    main()

