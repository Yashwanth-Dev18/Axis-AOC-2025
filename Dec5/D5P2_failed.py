# def cafeteria_part2():
#   ranges = []
#   with open('D5_input.txt') as f:
#     for line in f:
#       data = line.strip()
    
#       if data == "":
#         break
#       else:
#         parts = data.split("-")
#         ranges.append([int(parts[0]), int(parts[1])])

#   fresh_count = 0
#   fresh_lst = []
#   for i in range(len(ranges)):
#     for j in range(ranges[i][0], ranges[i][1] + 1):
#       if j not in fresh_lst:
#         fresh_lst.append(j)
#         fresh_count += 1
#       print(j)
#     print(i+1)

#   return fresh_count



# print(cafeteria_part2())
