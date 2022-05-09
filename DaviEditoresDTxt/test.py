from tkinter import *
import openai
from pyperclip3 import copy

openai.api_key = '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'
window = Tk()
window.title("Suggestions")
window.geometry("300x300")
window.resizable(0, 0)

def copy_and_close(txt):
    global window
    copy(txt)
    window.destroy()
    
def sugegstion(event=None, text='Quem é Bolsonaro?'):
    global window 
    Sugestion = openai.Completion.create(
      engine="text-davinci-002",
      prompt=text,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
)
    print(Sugestion.choices)
    
    #add sugestion to the window (above all the text will have one copy to clipboard botton)
    copy_button = Button(window, text="Copy", command=lambda: copy(Sugestion.choices[0].text))
    copy_button.pack()
    label = Label(window, text=Sugestion.choices[0].text)
    label.pack()
    window.mainloop()
sugegstion()