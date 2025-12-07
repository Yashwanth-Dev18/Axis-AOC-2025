def forklift():
  main_list = []
  rolls = 0
  with open("D4P1_input.csv") as f:
    for line in f:
      sequence = line.strip()
      sequence = list(sequence)
      main_list += [sequence]

    for i in range(len(main_list)):
      for j in range(len(main_list[i])):
        count = 0

        # Top left corner
        if i == 0 and j == 0:
          if main_list[i][j] == "@":
            rolls += 1
          continue
        
        # Bottom left corner
        elif i == len(main_list)-1 and j == 0:
          if main_list[i][j] == "@":
            rolls += 1
          continue

        # Bottom right corner
        elif i == len(main_list)-1 and j == len(main_list[i])-1:
          if main_list[i][j] == "@":
            rolls += 1
          continue
        
        # Top right corner
        elif i == 0 and j == len(main_list[i])-1:
          if main_list[i][j] == "@":
            rolls += 1
          continue

        # check first element of all rows except first row's and last row's first element
        elif j == 0 and i != 0 and i != len(main_list)-1:
          if main_list[i][j] == "@":
            if main_list[i-1][j] != None and main_list[i-1][j] == "@":
              count += 1
            if main_list[i+1][j] != None and main_list[i+1][j] == "@":
              count += 1
            if main_list[i][j+1] != None and main_list[i][j+1] == "@":
              count += 1
            if main_list[i-1][j+1] != None and main_list[i-1][j+1] == "@":
              count += 1
            if main_list[i+1][j+1] != None and main_list[i+1][j+1] == "@":
              count += 1
            if count < 4:
              rolls += 1
          
        # check last element of all rows except first row's and last row's last element
        elif j == len(main_list[i])-1 and i != 0 and i != len(main_list)-1:
          if main_list[i][j] == "@":
            if main_list[i-1][j] != None and main_list[i-1][j] == "@":
              count += 1
            if main_list[i+1][j] != None and main_list[i+1][j] == "@":
              count += 1
            if main_list[i][j-1] != None and main_list[i][j-1] == "@":
              count += 1
            if main_list[i-1][j-1] != None and main_list[i-1][j-1] == "@":
              count += 1
            if main_list[i+1][j-1] != None and main_list[i+1][j-1] == "@":
              count += 1
            if count < 4:
              rolls += 1
        
        # check first row except first and last element
        elif i == 0 and j != 0 and j != len(main_list[i])-1:
          if main_list[i][j] == "@":
            if main_list[i][j-1] != None and main_list[i][j-1] == "@":
              count += 1
            if main_list[i][j+1] != None and main_list[i][j+1] == "@":
              count += 1
            if main_list[i+1][j] != None and main_list[i+1][j] == "@":
              count += 1
            if main_list[i+1][j-1] != None and main_list[i+1][j-1] == "@":
              count += 1
            if main_list[i+1][j+1] != None and main_list[i+1][j+1] == "@":
              count += 1
            if count < 4:
              rolls += 1
        
        # check last row except first and last element
        elif i == len(main_list)-1 and j != 0 and j != len(main_list[i])-1:
          if main_list[i][j] == "@":
            if main_list[i][j-1] != None and main_list[i][j-1] == "@":
              count += 1
            if main_list[i][j+1] != None and main_list[i][j+1] == "@":
              count += 1
            if main_list[i-1][j] != None and main_list[i-1][j] == "@":
              count += 1
            if main_list[i-1][j-1] != None and main_list[i-1][j-1] == "@":
              count += 1
            if main_list[i-1][j+1] != None and main_list[i-1][j+1] == "@":
              count += 1
            if count < 4:
              rolls += 1
        

        # check all other elements
        elif main_list[i][j] == "@":
          if main_list[i-1][j] != None and main_list[i-1][j] == "@":
            count += 1
          if main_list[i+1][j] != None and main_list[i+1][j] == "@":
            count += 1
          if main_list[i][j-1] != None and main_list[i][j-1] == "@":
            count += 1
          if main_list[i][j+1] != None and main_list[i][j+1] == "@":
            count += 1
          if main_list[i-1][j-1] != None and main_list[i-1][j-1] == "@":
            count += 1
          if main_list[i-1][j+1] != None and main_list[i-1][j+1] == "@":
            count += 1
          if main_list[i+1][j-1] != None and main_list[i+1][j-1] == "@":
            count += 1
          if main_list[i+1][j+1] != None and main_list[i+1][j+1] == "@":
            count += 1
          if count < 4:
            rolls += 1

        else:
          continue

  return rolls

print(forklift())