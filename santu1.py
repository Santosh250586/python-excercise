import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it"

word = input("enter word: ")

print (translate(word))
