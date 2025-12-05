def password():
  num = 50
  zero_count = 0
  with open('D1P1_input.txt') as f:
    for line in f:
      pointer = line.strip()


      if pointer[0] == 'L':
        num = num - int(pointer[1:])
        num = num % 100
        if num == 0:
          zero_count += 1
      
      elif pointer[0] == 'R':
        num = num + int(pointer[1:])
        num = num % 100
        if num == 0:
          zero_count += 1
    
  return zero_count


print(password())