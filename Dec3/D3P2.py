def joltage():
    jolts = 0
    with open('Dec3/D3_input.txt') as f:
        for line in f:
            sequence = line.strip()
            
            current_string = ""
            last_index = -1 
            
            for i in range(12):
                
                remaining = 11 - i 
                
                start_search = last_index + 1
                end_search = len(sequence) - remaining
                
                index = start_search
                
                for j in range(start_search, end_search):
                    current_num = int(sequence[j])

                    if int(sequence[index]) < current_num:
                        index = j
                current_string += sequence[index]
                last_index = index

            jolts += int(current_string)
            

    return jolts

print(joltage())