import json

def isNullOrEmpty(obj):
    if not (obj is None or not obj):
        return False;

    return True;

def getNumberJSON():
    with open('numberPronous.json', 'r') as file:
        numbersJson = json.load(file)
        return numbersJson["numbers"]
