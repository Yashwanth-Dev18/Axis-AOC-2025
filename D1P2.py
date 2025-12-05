def password():
  num = 50
  zero_count = 0
  with open('D1_input.txt') as f:
    for line in f:
      pointer = line.strip()


      if pointer[0] == 'L':
        num_start = num
        num = num - int(pointer[1:])
        num = num % 100
        
        if num_start < int(pointer[1:]) and int(pointer[1:]) < 100:
          if num_start != 0:
            zero_count += 1
        elif num_start >= int(pointer[1:]):
          if num == 0:
            zero_count += 1
        elif num_start < int(pointer[1:]) and int(pointer[1:]) >= 100:
          zero_count += (((num_start - int(pointer[1:]))//100)*-1)
      
      elif pointer[0] == 'R':
        num_start = num
        num = num + int(pointer[1:])
        num = num % 100
        if num_start + int(pointer[1:]) >= 100 and int(pointer[1:]) < 100: 
          zero_count += 1
        elif int(pointer[1:]) >= 100:
          zero_count += ((num_start + int(pointer[1:]))//100)
      
      print(num)
      print(zero_count)
      print("-------")

    
  return zero_count
# veki veki song

print(password())