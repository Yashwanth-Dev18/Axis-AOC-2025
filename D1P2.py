def password():
  num = 50
  zero_count = 0
  with open('D1_decoy_input.txt') as f:
    for line in f:
      pointer = line.strip()


      if pointer[0] == 'L':
        num_start = num
        num = num - int(pointer[1:])
        
        distance_moved = num_start - num
        if distance_moved < 0:
          distance_moved = distance_moved * -1
        zero_count += distance_moved // 100

        num = num % 100
      
      elif pointer[0] == 'R':
        num_start = num
        num = num + int(pointer[1:])

        distance_moved = num - num_start
        if distance_moved < 0:
          distance_moved = distance_moved * -1
        zero_count += distance_moved // 100

        num = num % 100
      
      print(num)
      print(zero_count)
      print("-------")

    
  return zero_count
# veki veki song

print(password())