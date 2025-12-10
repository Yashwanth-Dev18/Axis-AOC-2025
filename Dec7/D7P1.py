def teleport():
  grid = []
  with open("D7_input.txt") as f:
    for line in f:
      temp_lst = []
      for i in line:
        temp_lst += i.split()
      grid.append(temp_lst)


  splits = 0
  beams = []
  temp_beams = []

  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "S":
        temp_beams.append(j)
        continue
      if grid[i][j] == "^":
        for k in beams:
          if k == j:
            splits += 1
            temp_beams.append(k-1)
            temp_beams.append(k+1)
            beams.remove(k)
          else:
            continue
      if grid[i][j] == ".":
        continue

    if temp_beams == []:
      continue
    else:
      for l in temp_beams:
          if l not in beams and 0 <= l < len(grid[i]):
            beams.append(l)
      temp_beams = []

  return splits


print(teleport())