import tkinter as tk
import tkinter.font as font
from translate import Translator
import googletrans
from tkinter import Button, ttk
import os
from PIL import Image, ImageTk
from pyperclip import copy



#add btton
def Translate():
    def language(x, text):
        global t
        translator = Translator(to_lang = x)
        t = translator.translate(text)
        textBox2.insert("1.0", t)


    def convert():
        global x
        x = choice.get()
        text = textBox1.get("1.0", tk.END)
        language(x,text)
    
    list1 = list(googletrans.LANGUAGES.values())
    list2 = list(googletrans.LANGUAGES.keys())

    DaviTradutores = tk.Tk( )
    DaviTradutores.title("Davi Tradutoes")
    DaviTradutores.configure(bg = "#000000")  # for background color
    ico = Image.open('icons/translate.png')
    photo = ImageTk.PhotoImage(ico)
    DaviTradutores.wm_iconphoto(False, photo)

    DaviTradutores.rowconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize = 35)
    DaviTradutores.columnconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize = 35)

    label = tk.Label(text = "Davi Tradutores", fg = "#000000" , bg = "#ffffff",
                    relief = tk.RIDGE, borderwidth = 5, font = "Verdana")
    label['font'] = font.Font(size= 18)
    label.grid(row = 0, column = 4, pady = 10, ipadx = 5, ipady = 5)

    label1 = tk.Label(text = "Tradução", fg = "#000000", bg = "#ffffff",
                    relief = tk.RIDGE, borderwidth = 2, font = "Verdana")
    label1.grid(row = 1, column = 7, ipadx = 5, ipady = 5)

    label1 = tk.Label(text = "Texto", fg = "#000000", bg = "#ffffff",
                    relief = tk.RIDGE, borderwidth = 2, font = "Verdana")
    label1.grid(row = 1, column = 1, ipadx = 5, ipady = 5)

    labelSelect = tk.Label(text = "IDIOMA:", fg = "#000000", bg = "#ffffff", font="Calibri")
    labelSelect.grid(row = 2, column = 4, ipadx = 5, ipady = 5)



    inst = tk.StringVar()
    choice = ttk.Combobox(DaviTradutores, width = 15, textvariable = inst)
    choice['values'] = list1
    choice.grid(row =3, column = 4 )
    choice.current()


        
    button1 = tk.Button(text = "Traduzir", fg = "#000000", bg = "#FFFFFF",activebackground = "#00FFF2",
                        relief = tk.RIDGE, borderwidth = 3, font = "Verdana", command = convert)
    button1.grid(row = 4, column = 4, ipadx = 5, ipady = 5)


    textBox1 = tk.Text( width = 35, height = 15, font = "Arial", relief = tk.SUNKEN, borderwidth = 3)
    textBox1.grid(row = 4, column = 1)

    textBox2 = tk.Text( width = 35, height = 15, font = "Arial", relief = tk.SUNKEN, borderwidth = 3)
    textBox2.grid(row = 4, column = 7)

    #set textbot1 and 2 to background color
    textBox1.configure(bg = "#000000")
    textBox2.configure(bg = "#000000")
    #set textbox1 and 2 to foreground color
    textBox1.configure(fg = "#FFFFFF")
    textBox2.configure(fg = "#FFFFFF")
    
    #bellow the textbox1 add one button to clear the textbox
    cleansButton = tk.Button(text = "Limpar", fg = "#000000", bg = "#FFFFFF",activebackground = "#00FFF2", relief = tk.RIDGE, borderwidth = 3, font = "Verdana", command = lambda: textBox1.delete("1.0", tk.END))
    cleansButton.grid(row = 5, column = 1, ipadx = 5, ipady = 5)

    #bellow the textbox2 add one button to copy the textbox
    copyButton = tk.Button(text = "Copiar", fg = "#000000", bg = "#FFFFFF",activebackground = "#00FFF2", relief = tk.RIDGE, borderwidth = 3, font = "Verdana", command = lambda: copy(textBox2.get("1.0", tk.END)))
    copyButton.grid(row = 5, column = 7, ipadx = 5, ipady = 5)
    
    DaviTradutores.mainloop()

Translate()