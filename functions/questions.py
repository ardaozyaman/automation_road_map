from question import Question
from gemini import *
import json
from packages.utils import *
'''
1. fonksiyon start
'''
def q1Func(min:int,max:int,div:int) -> list[int]:
    arrayRemain = []
    for i in range(min,max):
        if(i%div == 0):
            arrayRemain.append(i)
            print(i)
    return arrayRemain

'''
1. fonksiyon end
'''


'''
2. fonksiyon start
'''
numbersJson = getNumberJSON()
def q2Func(num:int=None,text:str=None):
    if not isNullOrEmpty(num):
        return numberToWords(num)
    elif not isNullOrEmpty(text):
        return wordsToNumber(text)
    else:
        return False

def numberToWords(num:int):
    if(num<10):
        return numbersJson[str(num)][str(1)]
    else:
        num_str = str(num)
        j = len(num_str)-1
        i = 0
        response=""
        for s in reversed(num_str):
            response += numbersJson[num_str[i]][str(j)] + " "
            i+=1
            j-=1

    return response

def wordsToNumber(text:str):
    response = 0
    words = []
    word = ""  
    
    for w in text:
        if not w == " ":
            word+=w
        else:
            if(not isNullOrEmpty(word)):
                words.append(word)
            word = ""

    if(not isNullOrEmpty(word)):
         words.append(word)

    if(len(words)>3):
         print(words)
         return False
    
    for w in words:
        for key1,val1 in numbersJson.items():
                   for key2,val2 in val1.items():
                           if w == val2:
                               response+=int(key1)* (10 ** int(key2))

    return str(response)

testText = "altıyüz yetmiş yedi"

print("benim zeka -> " + q2Func(text=testText))

print("AI (gemini-1.5-flash) yanıtı -> " + askAI(text=testText))

'''
2. fonksiyon end
'''

'''
3. fonksiyon start
'''
def examCalculate(vize1:int=0,vize2:int=0,final:int=0):
    notes = getNotesJSON()
    note=""
    if vize1 >= 0 and vize1 <= 100 and vize2 >= 0 and vize2 <= 100 and final >= 0 and final <= 100:
        totalNote=percenter(vize1,30)+percenter(vize2,30)+percenter(final,40)
        for key,value in notes.items():
            if(round(totalNote) >= int(key)):
                 note = value
                 break      
    else:
        return False
    
    print(round(totalNote))

    return note
    

print(examCalculate(55,55,100))

'''
3. fonksiyon end
'''