def compactor():
  data = []

  with open("D6_input.txt") as f:
    for line in f:
      items_lst = []
      items_lst += line.strip("\n")
      data += [items_lst]

  total = 0
  previous = 0
  for i in range(0, len(data[4])):
    if data[4][i] == " " and i != len(data[4]) - 1:
      continue

    elif i == 0:
      previous = i

    elif i == len(data[4]) - 1:
      digits = []
      for j in range(i, previous-1, -1):
        digits.append(data[0][j])
        digits.append(data[1][j])
        digits.append(data[2][j])
        digits.append(data[3][j])
        digits.append(".")
      digits.append(data[4][previous])

      nums = []
      num_str = ""
      for i in digits:
        if i not in [".", "+", "*", " "]:
          num_str += i
        elif i == ".":
          nums.append(int(num_str))
          num_str = ""
        elif i == "+":
          total += sum(nums)
          nums = []
        elif i == "*":
          product = 1
          for n in nums:
            product *= n
          total += product
          nums = []

    else:
      digits = []
      for j in range(i-2, previous-1, -1):
        digits.append(data[0][j])
        digits.append(data[1][j])
        digits.append(data[2][j])
        digits.append(data[3][j])
        digits.append(".")
      digits.append(data[4][previous])
      previous = i

      nums = []
      num_str = ""
      for i in digits:
        if i not in [".", "+", "*", " "]:
          num_str += i
        elif i == ".":
          nums.append(int(num_str))
          num_str = ""
        elif i == "+":
          total += sum(nums)
          nums = []
        elif i == "*":
          product = 1
          for n in nums:
            product *= n
          total += product
          nums = []
    
        
  return total
        


print(compactor())