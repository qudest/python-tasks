f = open("resources/in.txt", "r")
data = f.readlines()
f.close()

matrix = []
for line in data:
    row = line.strip("{ },\n")
    matrix.append([int(num.strip()) for num in row.split(", ")])

copy = [row[:] for row in matrix]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        copy[i][(j-1) % len(matrix[i])] = matrix[i][j]

f = open("resources/out.txt", "w")
f.write("{ ")
for i in range(len(copy)):
    if i == len(copy) - 1:
        f.write(str(copy[i]).replace("[", "{ ").replace("]", " }") + " }")
    else:
        f.write(str(copy[i]).replace("[", "{ ").replace("]", " }") + ",\n")
f.close()

