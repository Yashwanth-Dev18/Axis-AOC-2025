def quantum_teleport():
  grid = []
  with open("D7_input.txt") as f:
    for line in f:
      temp_lst = []
      for i in line:
        temp_lst += i.split()
      grid.append(temp_lst)
  
  timelines = [0] * len(grid[0])

  for i in range(len(grid[0])):
    if grid[0][i] == "S":
      timelines[i] = 1


  for i in range(1, len(grid)):
    temp_timelines = [0] * len(grid[0])

    for j in range(len(grid[i])):

      if timelines[j] == 0:
        continue

      if grid[i][j] == "^":
        if j - 1 >= 0:
          temp_timelines[j - 1] += timelines[j]
        if j + 1 < len(grid[i]):
          temp_timelines[j + 1] += timelines[j]
      
      elif grid[i][j] == ".":
        temp_timelines[j] += timelines[j]
    
    timelines = temp_timelines

  return sum(timelines)
  

print(quantum_teleport())
