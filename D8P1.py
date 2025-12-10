def playground():
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
  temp = []
  for i in range(1000):
    temp.append(distances[i])
  distances = []
  distances = temp

  circuits = []

  for distance in distances:
    boxA = distance[1]
    boxB = distance[2]
    in_circuit = False
    temp_circuit = []
    for circuit in circuits:
      if boxA in circuit or boxB in circuit:
        if boxA not in circuit:
          circuit.append(boxA)
        if boxB not in circuit:
          circuit.append(boxB)
        in_circuit = True
    
    if not in_circuit:
      circuits.append([boxA, boxB])


  merged = False
  while not merged:
    merged = True
      
    for i in range(len(circuits)):
      if not merged: 
        break
      
      for j in range(i + 1, len(circuits)):
        if set(circuits[i]) & set(circuits[j]):
          circuits[i] = list(set(circuits[i]) | set(circuits[j]))
          circuits.pop(j)
          merged = False 
          break
  

  circuits.sort(key=lambda x: len(x))
  product = len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3])
  return product


print(playground())