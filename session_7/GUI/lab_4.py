import tkinter as GUI
import math
main_window=GUI.Tk()
main_window.title("Welcome to Tkinter")
main_window.resizable(False,False)
main_window.geometry("450x450")


x_shift=0
y_shift=0
for i in range(4): 
    btn=GUI.Button(text="OK",width=20)
    btn.place(x=x_shift,y=y_shift)
    x_shift+=70
    y_shift+=25
main_window.mainloop()