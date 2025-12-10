def playground_pt2():
    data = []
    with open("D8_input.txt") as f:
        for line in f:
            data.append(line.strip().split(","))

    distances = []
    for i in range(len(data)-1):
        x1, y1, z1 = int(data[i][0]), int(data[i][1]), int(data[i][2])
        for j in range(i+1, len(data)):
            x2, y2, z2 = int(data[j][0]), int(data[j][1]), int(data[j][2])
            distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
            distances.append([distance, i, j])


    distances.sort(key=lambda x: x[0])

    circuits = []
    for i in range(len(data)):
        circuits.append([i])



    for distance in distances:
        boxA = distance[1]
        boxB = distance[2]
        
        index_A = -1
        index_B = -1

        for i in range(len(circuits)):
            if boxA in circuits[i]:
                index_A = i
            if boxB in circuits[i]:
                index_B = i
        
        if index_A != index_B:
            circuits[index_A].extend(circuits[index_B])
            circuits.pop(index_B)
            
            if len(circuits) == 1:
                x1 = int(data[boxA][0])
                x2 = int(data[boxB][0])
                return x1 * x2


print(playground_pt2())