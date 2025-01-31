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
    
def printClassInit(obj):
    print(str(obj.__class__.__name__)+" = "+ str((vars(obj)))+" -> init ")

def printClassDel(obj):
    print(str(obj.__class__.__name__)+" = "+ str((vars(obj)))+" -> deleted ")

def sectionPrinter(sectionText="section",content=""):
    chars2, chars1 = (">>>>","<<<<")
    print(chars1+" "+sectionText+" "+chars2, end="\n\n")
    print(str(content),end="\n\n")
    print(chars2+" "+sectionText+" "+chars1, end="\n\n")
