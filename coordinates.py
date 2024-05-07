x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x + 1)
               for j in range(y + 1)
               for k in range(z + 1)]
valid_coordinates = [coord for coord in coordinates if sum(coord) != n]

print(valid_coordinates)
