import google.generativeai as genai
GEMINI_API_KEY = "AIzaSyAO0G9aO7rhHrzAS8-9Wl1TqIV8klsRqss"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("65  yazıyla nasıl yazılır, sedece cevaplar")
print(response.text)