"""
Day 4 part 2 advent of code
by: Easton Seidel
"""


def remove_items(test_list, item): 
    # remove the item for all its occurrences 
    c = test_list.count(item) 
    for i in range(c):
        test_list.remove(item)
    return test_list 


def main():
    cards = 0
    number = 1
    win_num = []
    card_num = []
    card_wins = {}

    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()

    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-1]

    # Separate our card numbers and winning numbers
    for i in lines:
        win_num.append(remove_items(i.split(":")[1].split("|")[0].split(" "), ''))
        card_num.append(remove_items(i.split(":")[1].split("|")[1].split(" "), ''))
        card_wins[str(number)] = 1
        number += 1

    # See what our winnings are
    for i in range(len(card_num)):
        wins = 0

        for j in card_num[i]:
            if j in win_num[i]:
                wins += 1
        
        start = i + 2
        end = wins + start
        for j in range(start, end):
            card_wins[str(j)] += 1 * card_wins[str(i + 1)]
                
    # Get our total cards
    for i in card_wins:
        cards += card_wins[i]

    # Write the answer out to a file
    with open("day_4_2_output.txt", "w") as o:
        o.write(str(cards))


if __name__ == "__main__":
    main()
    