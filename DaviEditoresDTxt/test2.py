from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from tkinter import Entry

from openai import *

from openai.completion import *

from openai import api_requestor
from openai import pager
from openai import spec
from openai.tokenizer import tok
from openai import error

root = tk.Tk()
root.title("App")
root.geometry("500x500")

input_text = Entry(root, width=50)
input_text.pack()

texto = input_text.get()

def completar():
    completion = Completion()

    completion.model = 'davinci'
    completion.temperature = 0.7
    completion.max_tokens = 250
    
    completion.prompt = texto
    completion.top_p = 0.9
    
    response = completion.complete()

    for i in range(0,3):
        messagebox.showinfo(title="Sugestão", message=response[i]
