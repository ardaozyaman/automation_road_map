import json
from packages.utils import *
'''
Soru 1-start
'''
class Student:
    def __init__(self,name,surname,classNo):
        self.name = name
        self.surname = surname
        self.classNo = classNo
        printClassInit(self)

    def __del__(self):
        printClassDel(self)



class Question:
    def __init__(self,scorePerNet:int=2):
        self.scorePerNet = scorePerNet
        self.score = 0
        self.netScore = 0
        printClassInit(self)

    def __del__(self):
        printClassDel(self)

    def netCount(self,true:int=0,false:int=0):
        response = true - (false/4)
        self.netScore = response
        print(response)
        return response

    def calculate(self,netScore):
        response = netScore*self.scorePerNet
        print(response)
        return response
    
#que = Question()

#que.calculate(que.netCount(5,2))

'''
soru-1 end
'''

'''
soru-2 start
'''
class Person:
    def __init__(self,name:str,surname:str,age:int,country:str,city:str):
        self._name=name
        self._surname=surname
        self._age=age
        self._country=country
        self._city=city
        self._abilities = []

    def printAllPersonData(self):
       for key,value in vars(self).items():
           print(key+" : "+ str(value))

    def addAbility(self,ability:str):
        self._abilities.append(ability)


'''
soru-2 end
'''

