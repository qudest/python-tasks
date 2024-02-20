def are_similar(t1, t2):
    triangle1_sorted = sorted(t1)
    triangle2_sorted = sorted(t2)
    ratios = [triangle1_sorted[i] / triangle2_sorted[i] for i in range(3)]
    return all(ratio == ratios[0] for ratio in ratios)


f = open("resources/in.txt", "r")
triangles = []
for line in f:
    triangle = line.strip("\n").split(" ")
    triangle = [int(x) for x in triangle]
    triangles.append(triangle)
f.close()

result = []
for triangle1 in triangles:
    similar = [triangle1]
    for triangle2 in triangles:
        if (are_similar(triangle1, triangle2)) and (triangle1 != triangle2):
            similar.append(triangle2)
    result.append(similar)

for i in range(len(result)):
    result[i] = sorted(result[i], key=lambda x: sum(x))
unique = []
for triangles in result:
    if triangles not in unique:
        unique.append(triangles)

f = open("resources/out.txt", "w")
for line in unique:
    f.write(str(line) + "\n")
f.close()

