from tkinter import *
from datetime import date

window = Tk()
window.title("First Tkinter")
window.geometry("800x400")
window.configure(bg="lightblue")

lbl1 = Label(window, text="Hey there!", fg="white", bg="darkgreen", width=40, font=("Times New Roman", 20))
lbl1.pack()
lbl2 = Label(window, text="Enter your name:", fg="white", bg="darkgreen", width=30, font=("Times New Roman", 20))
lbl2.pack(pady=15)
name = Entry(width=30, font=("Times New Roman", 15))
name.pack(pady=5)
def display():
    get_name = name.get()
    global msg
    msg = f"Hello {get_name}\n"
    txt.insert(END, msg)
    txt.insert(END, f"Todays date is {date.today()}")
btn1 = Button(window, text="OK", command=display, font=("Times New Roman", 17))
btn1.pack(pady=10)
txt = Text(height=2, font=("Times New Roman", 15))
txt.pack()

window.mainloop()