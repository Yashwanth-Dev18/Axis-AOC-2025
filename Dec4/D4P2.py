def forklift_part2():
    main_list = []
    rolls = 0
    
    # Read file
    with open("D4P1_input.csv") as f:
        for line in f:
            sequence = line.strip()
            sequence = list(sequence)
            main_list += [sequence]


    while True:
        to_remove = [] # A list to store coordinates (i, j) that we will remove
        

        for i in range(len(main_list)):
            for j in range(len(main_list[i])):
                
                if main_list[i][j] != "@":
                    continue

                count = 0
                should_remove = False # A flag to decide if we keep this one


                # Corners
                if i == 0 and j == 0:
                    should_remove = True
                elif i == len(main_list)-1 and j == 0:
                    should_remove = True
                elif i == len(main_list)-1 and j == len(main_list[i])-1:
                    should_remove = True
                elif i == 0 and j == len(main_list[i])-1:
                    should_remove = True

                # Left Edge
                elif j == 0 and i != 0 and i != len(main_list)-1:
                    if main_list[i-1][j] == "@": count += 1
                    if main_list[i+1][j] == "@": count += 1
                    if main_list[i][j+1] == "@": count += 1
                    if main_list[i-1][j+1] == "@": count += 1
                    if main_list[i+1][j+1] == "@": count += 1
                    if count < 4: should_remove = True
            
                # Right Edge
                elif j == len(main_list[i])-1 and i != 0 and i != len(main_list)-1:
                    if main_list[i-1][j] == "@": count += 1
                    if main_list[i+1][j] == "@": count += 1
                    if main_list[i][j-1] == "@": count += 1
                    if main_list[i-1][j-1] == "@": count += 1
                    if main_list[i+1][j-1] == "@": count += 1
                    if count < 4: should_remove = True
            
                # Top Edge
                elif i == 0 and j != 0 and j != len(main_list[i])-1:
                    if main_list[i][j-1] == "@": count += 1
                    if main_list[i][j+1] == "@": count += 1
                    if main_list[i+1][j] == "@": count += 1
                    if main_list[i+1][j-1] == "@": count += 1
                    if main_list[i+1][j+1] == "@": count += 1
                    if count < 4: should_remove = True
            
                # Bottom Edge
                elif i == len(main_list)-1 and j != 0 and j != len(main_list[i])-1:
                    if main_list[i][j-1] == "@": count += 1
                    if main_list[i][j+1] == "@": count += 1
                    if main_list[i-1][j] == "@": count += 1
                    if main_list[i-1][j-1] == "@": count += 1
                    if main_list[i-1][j+1] == "@": count += 1
                    if count < 4: should_remove = True
            
                # Middle
                else:
                    if main_list[i-1][j] == "@": count += 1
                    if main_list[i+1][j] == "@": count += 1
                    if main_list[i][j-1] == "@": count += 1
                    if main_list[i][j+1] == "@": count += 1
                    if main_list[i-1][j-1] == "@": count += 1
                    if main_list[i-1][j+1] == "@": count += 1
                    if main_list[i+1][j-1] == "@": count += 1
                    if main_list[i+1][j+1] == "@": count += 1
                    if count < 4: should_remove = True
                
                if should_remove:
                    to_remove.append((i, j))

        if len(to_remove) == 0:
            break

        rolls += len(to_remove)
        
        for coordinate in to_remove:
            r = coordinate[0]
            c = coordinate[1]
            main_list[r][c] = "." # Turning paper into empty space

    return rolls

print(forklift_part2())