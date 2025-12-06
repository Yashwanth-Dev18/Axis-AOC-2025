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
        index = 1
        num_str = str(num)

        if len(num_str) % 2 != 0:
          divider = 3
        else:
          divider = 2

        while index <= len(num_str)//divider:
          test = ""
          repetition = 0
          while len(test) < len(num_str):
            repetition += 1
            test = num_str[:index]*repetition
          if test == num_str:
            sum += num
            break
          else:
            index += 1
        

  return sum

print(verify())