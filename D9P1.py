def theatre():
  coordinates = []
  with open('D9_input.txt') as f:
    for line in f:
      coordinates += [line.strip().split(',')]

  largest_area = 0
  for i in range(len(coordinates)-1):
    row1, col1 = int(coordinates[i][1]), int(coordinates[i][0])
    for j in range(i+1, len(coordinates)):
      row2, col2 = int(coordinates[j][1]), int(coordinates[j][0])
      length = abs(row2 - row1) + 1
      width = abs(col2 - col1) + 1
      area = length * width
      if area > largest_area:
        largest_area = area
  
  return largest_area
  

print(theatre())
