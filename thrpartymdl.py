import time
import os
import pandas

while True:
    if os.path.exists("original.csv"):
        data = pandas.read_csv("original.csv")
        print(data.mean()["str1"])
    else:
        print("File missing")
    time.sleep(5)
