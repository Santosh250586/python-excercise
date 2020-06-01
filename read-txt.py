myfile = open("santu.txt")
print (myfile.read())

print(" ")
print(" ")

file = open("fruit.txt")
content = file.read()
file.close()

with open("fruit.txt") as file:
    content = file.read()

print(content)
