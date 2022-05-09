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
    
    
    
#------------------------------------------------------------------------------------------------------------   
import tkinter as tk
from tkinter import messagebox
import json
from functools import partial
import requests

root = tk.Tk()
root.title('Text Generator')

# get text from openai api
def get_text():
    url = 'https://api.openai.com/v1/engines/davinci/completions'
    # get the parameters from the input field
    params = {
        'max_tokens': 3,
        'temperature': 1,
        'top_p': 0.9,
        'n': 3,
        'stream': 'false',
        'logprobs': None,
        'stop': '\n',
        'prefix': input_field.get('1.0', tk.END),
        'presence_penalty': 0.0,
        'frequency_penalty': 0.0,
    }
    # send the parameters to openai api and get the response
    response = requests.post(url, json=params)
    # format the response
    text = json.loads(response.text)['choices']
    # create a window with the suggestions
    suggestions_window = tk.Toplevel(root)
    suggestions_window.title('Suggestions')
    # create a button for each suggestion
    for index, suggestion in enumerate(text):
        # create the function that adds the suggestion to the input field and destroys the suggestions window
        def add_suggestion(s):
            input_field.insert('end', s)
            suggestions_window.destroy()
        # create the button with the suggestion
        tk.Button(suggestions_window, text=suggestion['text'], command=partial(add_suggestion, suggestion['text'])).grid()

# create the input field
input_field = tk.Text(root, height=10, width=40)
input_field.grid(row=0, column=0)
# create the button that generates suggestions
tk.Button(root, text='Generate suggestions', command=get_text).grid(row=1, column=0)

root.mainloop()
    
    response = completion.complete()

    for i in range(0,3):
        messagebox.showinfo(title="Sugestão", message=response[i]
