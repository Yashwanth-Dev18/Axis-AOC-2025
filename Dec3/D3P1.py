def joltage():
  with open('D3_input.txt') as f:
    jolts = 0
    for line in f:
      sequence = line.strip()

      index1 = 0
      for i in range(len(sequence) - 1):
        current_num = int(sequence[i])
        if int(sequence[index1]) < current_num:
          index1 = i

      index2 = i + 1
      for i in range(index1 + 1, len(sequence)):
        current_num = int(sequence[i])
        if int(sequence[index2]) < current_num:
          index2 = i

      jolts += ((int(sequence[index1])*10) + int(sequence[index2]))
    
  return jolts


print(joltage())
  