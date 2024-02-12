import tkinter as GUI
import math
main_window=GUI.Tk()
main_window.title("Welcome to Tkinter")
main_window.resizable(False,False)
main_window.geometry("450x450")

## functions 
def print_name():
    print("my name is ahmed")
def print_ok():
    print("ok")
def close_window():
    main_window.destroy()

### printing name buttin 
btn_1=GUI.Button(text="print name",bg="blue",command=print_name)
btn_1.place(x=20,y=20)

###  printing ok button 
btn_2=GUI.Button(text="ok",bg="green",command=print_ok)
btn_2.place(x=150,y=70)


## close window button 
btn_3=GUI.Button(text="close",bg="red",command=close_window)
btn_3.place(x=200,y=70)







main_window.mainloop()