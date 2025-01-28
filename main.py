import tkinter as tk
from question import Question
import openai

root = tk.Tk()
root.title("kpi")
root.geometry("300x200")  
label = tk.Label(root, text="Merhaba, Tkinter!")
label.pack(pady=20)

def on_button_click():
    label.config(text="Düğmeye Tıkladınız!")

button = tk.Button(root, text="Tıkla", command=on_button_click)
button.pack()

# Pencereyi göster
root.mainloop()


    
