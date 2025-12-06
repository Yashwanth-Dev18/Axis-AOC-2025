
def verify():
  with open("D2P1_input.txt") as f:
    sum = 0

    for line in f:
      data = line.split(",")
    
    for id_range in data:
      id_range = id_range.split("-")
      start = int(id_range[0])
      end = int(id_range[1])

      for num in range(start, end + 1):
        num_str = str(num)
        splitter = (len(num_str) // 2)
        first_half = num_str[:splitter]
        second_half = num_str[splitter:]
        if first_half == second_half:
          sum += num

  return sum



print(verify())