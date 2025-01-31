from functions.question import Question
from gemini import *
from packages.utils import *
from time import sleep
import json


class Questions:
    def __init__(self):
        self.numbersJson = getNumberJSON()

    """
    1. fonksiyon start
    """

    def q1Func(self, min: int, max: int, div: int) -> list[int]:
        name = "soru 1"
        arrayRemain = []
        for i in range(min, max):
            if i % div == 0:
                arrayRemain.append(i)
        sectionPrinter(name, content=arrayRemain)
        return arrayRemain

    """
    1. fonksiyon end
    """

    """
    2. fonksiyon start
    """

    def q2Func(self, num: int = None, text: str = None, aiCompare: bool = True):
        name = "soru 2"
        response = ""
        aiResponse = ""
        if not isNullOrEmpty(num):
            response = self._numberToWords(num)
        elif not isNullOrEmpty(text):
            response = self._wordsToNumber(text)
        else:
            response = "geçerli bir input giriniz"
        if aiCompare:
            aiResponse = "AI (gemini-1.5-flash) -> " + askAI(num=num, text=text)

        sectionPrinter(name, content=response + "\n\n" + aiResponse)
        return response

    def _numberToWords(self, num: int):
        if num < 10:
            return self.numbersJson[str(num)][str(1)]
        else:
            num_str = str(num)
            j = len(num_str) - 1
            i = 0
            response = ""
            for s in reversed(num_str):
                response += self.numbersJson[num_str[i]][str(j)] + " "
                i += 1
                j -= 1

        return response

    def _wordsToNumber(self, text: str):
        response = 0
        words = []
        word = ""

        for w in text:
            if not w == " ":
                word += w
            else:
                if not isNullOrEmpty(word):
                    words.append(word)
                word = ""

        if not isNullOrEmpty(word):
            words.append(word)

        if len(words) > 3:
            print(words)
            return False

        for w in words:
            for key1, val1 in self.numbersJson.items():
                for key2, val2 in val1.items():
                    if w == val2:
                        response += int(key1) * (10 ** int(key2))

        return str(response)

    """
    2. fonksiyon end
    """

    """
    3. fonksiyon start
    """

    def examCalculate(self, vize1: int = 0, vize2: int = 0, final: int = 0):
        name = "soru 3"
        notes = getNotesJSON()
        note = ""
        if (
            vize1 >= 0
            and vize1 <= 100
            and vize2 >= 0
            and vize2 <= 100
            and final >= 0
            and final <= 100
        ):
            totalNote = (
                percenter(vize1, 30) + percenter(vize2, 30) + percenter(final, 40)
            )
            for key, value in notes.items():
                if round(totalNote) >= int(key):
                    note = value
                    break
        else:
            return False
        sectionPrinter(name, content=note)
        return note

    """
    3. fonksiyon end
    """
