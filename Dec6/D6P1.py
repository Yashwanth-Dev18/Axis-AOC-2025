def compactor():
  data = []
  with open("D6_input.txt") as f:
    for line in f:
      items_lst = line.strip().split(" ")

      temp_lst = []
      for i in items_lst:
        if i != "" and i != "+" and i != "*":
          temp_lst.append(int(i))
        elif i == "+" or i == "*":
          temp_lst.append(i)
        
      data += [temp_lst]

  total = 0
  for i in range(len(data[4])):
    if data[4][i] == "+":
      total += data[0][i] + data[1][i] + data[2][i] + data[3][i]
    elif data[4][i] == "*":
      total += (data[0][i] * data[1][i] * data[2][i] * data[3][i])


  return total


print(compactor())