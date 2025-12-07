def cafeteria():
  ranges = []
  stock = []
  is_first_section = True

  with open("D5_input.txt") as f:
    for line in f:
      data = line.strip()

      if data == "":
        is_first_section = False
        continue
      
      if is_first_section:
        ranges.append(data)
      else:
        stock.append(data)


    for i in range(len(ranges)):
      parts = ranges[i].split("-")
      ranges[i] = [int(parts[0]), int(parts[1])]
    
    for i in range(len(stock)):
      stock[i] = int(stock[i])

  fresh_count = 0
  for i in stock:
    for j in ranges:
      if i >= j[0] and i <= j[1]:
        fresh_count += 1
        break
      else:
        continue

  return fresh_count
        


print(cafeteria())