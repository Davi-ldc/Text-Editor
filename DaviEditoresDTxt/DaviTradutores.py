import tkinter as tk
import tkinter.font as font
import googletrans
from tkinter import Button, ttk
from PIL import Image, ImageTk
from pyperclip import copy
import pyttsx3



#add btton
def Translate() -> None:
    def language(text, to_lang='en', from_lang='pt'):
        global t
        translated_text = googletrans.Translator().translate(text, src=from_lang, dest=to_lang).text
        textBox2.insert("1.0", translated_text)


    def convert():
        global x
        to_lang = to_lang_choice.get()
        from_lang = from_lang_choice.get()
        text = textBox1.get("1.0", tk.END)
        tranlated_text_box = textBox2.get("1.0", tk.END)
        if 'Aqui aparecerá a tradução' in tranlated_text_box or 'Escolha um indioma' in tranlated_text_box:
            textBox2.delete("1.0", tk.END)
            if to_lang == '' or from_lang == '':
                textBox2.insert("1.0", 'Escolha um indioma')
        language(text, to_lang=to_lang, from_lang=from_lang)
    
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
    label1.grid(row = 0, column = 7, ipadx = 5, ipady = 5)

    label1 = tk.Label(text = "Texto", fg = "#000000", bg = "#ffffff",
                    relief = tk.RIDGE, borderwidth = 2, font = "Verdana")
    label1.grid(row = 0, column = 1, ipadx = 5, ipady = 5)

    #bellow label1 add one text:
    to_lang_text = tk.Label(text = "Para:", fg = "#000000", bg = "#ffffff")
    to_lang_text.grid(row = 2, column = 7, ipadx = 5, ipady = 5)

    #bellow label1 add one text:
    from_lang_text = tk.Label(text = "De:", fg = "#000000", bg = "#ffffff")
    from_lang_text.grid(row = 2, column = 1, ipadx = 5, ipady = 5)
    
    #to lang select
    inst = tk.StringVar()
    to_lang_choice = ttk.Combobox(DaviTradutores, width = 15, textvariable = inst)
    to_lang_choice['values'] = list1
    to_lang_choice.grid(row =3, column = 7)
    to_lang_choice.current()
    
    #from lang select
    inst = tk.StringVar()
    from_lang_choice = ttk.Combobox(DaviTradutores, width = 15, textvariable = inst)
    from_lang_choice['values'] = list1
    from_lang_choice.grid(row =3, column = 1)
    from_lang_choice.current()

        
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
    

    cleansButton = tk.Button(text = "Limpar", fg = "#000000", bg = "#FFFFFF",activebackground = "#00FFF2", relief = tk.RIDGE, borderwidth = 3, font = "Verdana", command = lambda: textBox1.delete("1.0", tk.END))
    cleansButton.grid(row = 5, column = 1, ipadx = 5, ipady = 5)
    
    engine = pyttsx3.init()
    def speak(val): 
        engine.say({val})
        engine.runAndWait()
        
    speak_icon = ImageTk.PhotoImage(file='icons/audio.png')
    # button to speak the textbox1
    #speak_button1 = tk.Button(DaviTradutores, text='Falar', command = lambda: speak(textBox1.get("1.0", tk.END)))
    #speak_button1.grid(row = 5, column = 7, ipadx = 5, ipady = 5)
    
    # #button to speak the textbox2
    # speak_button2 = tk.Button(DaviTradutores, image = speak_icon, command = lambda: speak(textBox2.get("1.0", tk.END)))
    # speak_button2.grid(row = 5, column = 4, ipadx = 5, ipady = 5)
    
    #button to copy the textbox
    copyButton = tk.Button(text = "Copiar", fg = "#000000", bg = "#FFFFFF",activebackground = "#00FFF2", relief = tk.RIDGE, borderwidth = 3, font = "Verdana", command = lambda: copy(textBox2.get("1.0", tk.END)))
    copyButton.grid(row = 5, column = 7, ipadx = 5, ipady = 5)
    

    
    textBox1.insert("1.0", """Digite o texto que será traduzido  """)
    textBox2.insert("1.0", """Aqui aparecerá a tradução  """)
    
    DaviTradutores.mainloop()




Translate()