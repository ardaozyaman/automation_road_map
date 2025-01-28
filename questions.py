from question import Question
import json
from utils import *

def q1Func(min:int,max:int,div:int) -> list[int]:
    arrayRemain = []
    for i in range(min,max):
        if(i%div == 0):
            arrayRemain.append(i)
            print(i)
    return arrayRemain


numbersJson = getNumberJSON()

def q2Func(num:int=None,text:str=None):
    if not isNullOrEmpty(num):
        return numberToWords(num)
    elif not isNullOrEmpty(text):
        pass
    else:
        return False

def numberToWords(num:int):
    if(num<10):
        return numbersJson[str(num)][str(1)]
    else:
        num_str = str(num)
        j = len(num_str)
        i = 0
        response=""
        for s in reversed(num_str):
            response += numbersJson[num_str[i]][str(j)] + " "
            i+=1
            j-=1

    return response

def wordsToNumber(text:str):
    print(text)

print(q2Func())

for key,value in numbersJson.items():
    if (value["2"] == "doksan"):
        print(key)
