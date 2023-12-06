"""
Day 3 advent of code
By: Easton Seidel
"""


def remove_items(test_list, item): 
    # remove the item for all its occurrences 
    c = test_list.count(item) 
    for i in range(c):
        test_list.remove(item)
    return test_list 


def main():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n']
    sum = 0
    e = None
    
    # Read our input
    with open("../input.txt") as i:
        lines = i.readlines()
        
    # Loop through the range of the lines
    for i in range(len(lines)):
        # Pull current line stats
        print(f"\nStep {i + 1}\nCurrent working line: {lines[i]}")
        j = 0
        
        while j < len(lines[i]):
            symbol_array = []
            
            # A single num
            try:
                int(lines[i][j])
                
                # Start of num s and end of num e
                s = j
                e = j + 1
                # A second num
                try:
                    int(lines[i][j:j+2])
                    
                    e = j + 2
                    # A third num
                    try:
                        int(lines[i][j:j+3])
                        
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
            for k in nums:
                symbol_array = remove_items(symbol_array, k)

            if len(symbol_array) > 0:
                print(symbol_array)
                sum += int(lines[i][s:e])
                print(f"Number {lines[i][s:e]} added. New sum is {sum}")
                j = e
                e = None
            elif e is not None:
                j = e
                e = None
            else:
                j += 1
    # Write the answer out to a file
    with open("day_3_output.txt", "w") as o:
        print(f"\nFinal sum: {sum}")
        o.write(str(sum))
    
    
if __name__ == "__main__":
    main()
        