import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("200x100")

# add one bar with number (0.0 - 1.0) for the user select
#number need to be float with 1 decimal case
#default value is 0.0
slider = tk.Scale(window, from_=0.0, to=1.0, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=0.1, resolution=0.1, command=print)
slider.pack()
  
def select():  
   sel = "Value = " + str(v.get())  
   label.config(text = sel)  
     
top = tk.Tk()  
top.geometry("200x100")  
v = tk.DoubleVar()  
scale = tk.Scale( top, variable = v, from_ = 1, to = 50, orient = tk.HORIZONTAL)  
scale.pack(anchor=tk.CENTER)  
  
btn = tk.Button(top, text="Value", command=select)  
btn.pack(anchor=tk.CENTER)  
  
label = tk.Label(top)  
label.pack()  
  
top.mainloop()  
  


window.mainloop()