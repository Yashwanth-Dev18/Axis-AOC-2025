def password():
    num = 50
    zero_count = 0
    
    with open('D1_input.txt') as f:
        for line in f:
            pointer = line.strip()
            distance = int(pointer[1:])

            if pointer[0] == 'L':
                pos = (100 - num) % 100
                zero_count += (pos + distance) // 100
                num = (num - distance) % 100
      
            elif pointer[0] == 'R':
                zero_count += (num + distance) // 100
                num = (num + distance) % 100
      

    return zero_count

print(password())