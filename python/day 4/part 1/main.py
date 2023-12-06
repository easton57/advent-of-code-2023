"""
Day 4 advent of code
by: Easton Seidel
"""


def remove_items(test_list, item): 
    # remove the item for all its occurrences 
    c = test_list.count(item) 
    for i in range(c):
        test_list.remove(item)
    return test_list 


def main():
    points = 0
    win_num = []
    card_num = []
    
    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()
        
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-1]
    
    # Separate our card numbers and winning numbers
    for i in lines:
        win_num.append(remove_items(i.split(":")[1].split("|")[0].split(" "), ''))
        card_num.append(remove_items(i.split(":")[1].split("|")[1].split(" "), ''))
        
    # See what our winnings are
    for i in range(len(card_num)):
        winnings = 0
        
        for j in card_num[i]:
            if j in win_num[i] and winnings == 0:
                winnings += 1
            elif j in win_num[i] and winnings > 0:
                winnings *= 2
            
        points += winnings

    # Write the answer out to a file
    with open("day_4_output.txt", "w") as o:
        o.write(str(points))


if __name__ == "__main__":
    main()
    