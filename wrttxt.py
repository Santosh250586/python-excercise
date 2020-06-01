with open("veg.txt", "w") as myfile:
    myfile.write("Tomato\ncucumber\nonion\ngarlic\npotato")

with open("fruit.txt")as myfile:
    content = myfile.read()

with open("sham.txt", "w")as mfile:
    mfile.write(content[:20])
    