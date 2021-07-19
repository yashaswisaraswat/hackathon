
import json
import random

with open("train.json", "r") as rf:
    decoded_data = json.load(rf)
rec=input("Enter a cuisine : ")
l=[]
for x in decoded_data:
    cuisine = x.get("cuisine")

    if rec == cuisine:
        l.append(x.get("ingredients"))
        
print(random.choice(l))
print("total recipe : ",len(l))