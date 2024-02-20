f = open("resources/in.txt", "r")
data = f.read()
f.close()

data = data.replace("(", "").replace(")", "").replace("{", "").replace("}", "")
numbers = [int(num.strip()) for num in data.split(",")]
n = numbers.pop()

copy = numbers.copy()
for i in range(len(numbers)):
    copy[(i+n) % len(numbers)] = numbers[i]

f = open("resources/out.txt", "w")
f.write(str(copy).replace("[", "{ ").replace("]", " }"))
f.close()

