import google.generativeai as genai
from utils import *
GEMINI_API_KEY = "AIzaSyAO0G9aO7rhHrzAS8-9Wl1TqIV8klsRqss"


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def askAI(num:int=None,text:str=None):
    prompt = ""
    if not isNullOrEmpty(num):
         prompt = str(num) +" yazıyla (sözel olarak) nasıl yazılır, sedece cevaplar"
    elif not isNullOrEmpty(text):
        prompt = text + " rakam ile nasıl yazılır, sedece cevaplar"
    else:
        return False
    response = model.generate_content(prompt)
    
    return response.text