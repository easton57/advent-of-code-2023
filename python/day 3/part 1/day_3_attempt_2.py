"""
Day 3 advent of code
By: Easton Seidel
"""

sum = 0
lines = None


def remove_items(test_list, item): 
    # remove the item for all its occurrences 
    c = test_list.count(item) 
    for i in range(c): 
        test_list.remove(item) 
    return test_list 


def main():
    global sum
    global lines
    
    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()
        
    # Loop through the range of the lines
    for i in range(len(lines)):
        # Pull current line stats
        print(f"\nStep {i + 1}\nCurrent working line: {lines[i]}")
        
        for j in range(len(lines[i])):
            symbol_array = []
            
            # A single num
            try:
                int(lines[i][j])
                
                # Start of num s and end of num e
                s = j
                e = j + 1
                # A second num
                try:
                    int(lines[i][j:j+1])
                    
                    e = j + 2
                    # A third num
                    try:
                        int(lines[i][j:j+2])
                        
                        e = j + 3
                        
                        # triple num result
                        # check the edges on the line (x axis) (x axis)
                        if j == 0:
                            symbol_array.append(lines[i][e])
                        elif j == len(lines[i]) - 1:
                            symbol_array.append(lines[i][j - 1])
                        else:
                            symbol_array.append(lines[i][e])
                            symbol_array.append(lines[i][j - 1])

                        # Check the edges of the page (y axis)
                        if i == 0:
                            symbol_array.append(lines[i + 1][j - 1])
                            symbol_array.append(lines[i + 1][j])
                            symbol_array.append(lines[i + 1][j + 1])
                            symbol_array.append(lines[i + 1][j + 2])
                            symbol_array.append(lines[i + 1][e])
                        elif i == len(lines) - 1:
                            symbol_array.append(lines[i - 1][j - 1])
                            symbol_array.append(lines[i - 1][j])
                            symbol_array.append(lines[i - 1][j + 1])
                            symbol_array.append(lines[i - 1][j + 2])
                            symbol_array.append(lines[i - 1][e])
                        else:
                            symbol_array.append(lines[i + 1][j - 1])
                            symbol_array.append(lines[i + 1][j])
                            symbol_array.append(lines[i + 1][j + 1])
                            symbol_array.append(lines[i + 1][j + 2])
                            symbol_array.append(lines[i + 1][e])
                            symbol_array.append(lines[i - 1][j - 1])
                            symbol_array.append(lines[i - 1][j])
                            symbol_array.append(lines[i - 1][j + 1])
                            symbol_array.append(lines[i - 1][j + 2])
                            symbol_array.append(lines[i - 1][e])
                    except ValueError:  # Double Num result
                        # check the edges on the line (x axis) (x axis)
                        if j == 0:
                            symbol_array.append(lines[i][e])
                        elif j == len(lines[i]) - 1:
                            symbol_array.append(lines[i][j - 1])
                        else:
                            symbol_array.append(lines[i][e])
                            symbol_array.append(lines[i][j - 1])
    
                        # Check the edges of the page (y axis)
                        if i == 0:
                            symbol_array.append(lines[i + 1][j - 1])
                            symbol_array.append(lines[i + 1][j])
                            symbol_array.append(lines[i + 1][j + 1])
                            symbol_array.append(lines[i + 1][e])
                        elif i == len(lines) - 1:
                            symbol_array.append(lines[i - 1][j - 1])
                            symbol_array.append(lines[i - 1][j])
                            symbol_array.append(lines[i - 1][j + 1])
                            symbol_array.append(lines[i - 1][e])
                        else:
                            symbol_array.append(lines[i + 1][j - 1])
                            symbol_array.append(lines[i + 1][j])
                            symbol_array.append(lines[i + 1][j + 1])
                            symbol_array.append(lines[i + 1][e])
                            symbol_array.append(lines[i - 1][j - 1])
                            symbol_array.append(lines[i - 1][j])
                            symbol_array.append(lines[i - 1][j + 1])
                            symbol_array.append(lines[i - 1][e])
                except ValueError:  # single num result
                    # check the edges on the line (x axis)
                    if j == 0:
                        symbol_array.append(lines[i][e])
                    elif j == len(lines[i]) - 1:
                        symbol_array.append(lines[i][j - 1])
                    else:
                        symbol_array.append(lines[i][e])
                        symbol_array.append(lines[i][j - 1])
                        
                    # Check the edges of the page (y axis)
                    if i == 0:
                        symbol_array.append(lines[i + 1][j - 1])
                        symbol_array.append(lines[i + 1][j])
                        symbol_array.append(lines[i + 1][e])
                    elif i == len(lines) - 1:
                        symbol_array.append(lines[i - 1][j - 1])
                        symbol_array.append(lines[i - 1][j])
                        symbol_array.append(lines[i - 1][e])
                    else:
                        symbol_array.append(lines[i - 1][j - 1])
                        symbol_array.append(lines[i - 1][j])
                        symbol_array.append(lines[i - 1][e])
                        symbol_array.append(lines[i + 1][j - 1])
                        symbol_array.append(lines[i + 1][j])
                        symbol_array.append(lines[i + 1][e])
            except ValueError:  # not a number
                pass
            
            # Check for symbols and add the shiz to the total
            symbol_array = remove_items(symbol_array, ".")
            if len(symbol_array) > 0:
                sum += lines[i][s:e]
    # Write the answer out to a file
    with open("day_3_output.txt", "w") as o:
        print(f"\nFinal sum: {sum}")
        o.write(str(sum))
    
    
if __name__ == "__main__":
    main()
        