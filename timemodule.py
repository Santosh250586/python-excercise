import time

while  True:
      with open("veg.txt")as file:
          print(file.read())
          time.sleep(10)
          print("")
          
      