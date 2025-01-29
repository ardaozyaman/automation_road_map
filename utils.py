import json

def isNullOrEmpty(obj):
    if not (obj is None or not obj):
        return False;

    return True;

def getNumberJSON():
    with open('datas/numberPronous.json', 'r') as file:
        numbersJson = json.load(file)
        return numbersJson["numbers"]

def percenter(num:int=0,percent:int=0):
    return num/100*percent

def getNotesJSON():
    with open('datas/notes.json', 'r') as file:
        notesJson = json.load(file)
        return notesJson