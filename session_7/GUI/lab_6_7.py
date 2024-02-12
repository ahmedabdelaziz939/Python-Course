import tkinter as GUI
import math
main_window=GUI.Tk()
main_window.title("Welcome to Tkinter")
main_window.resizable(False,False)
main_window.geometry("450x450")

## creating label for username
label_1=GUI.Label(text="username")
label_1.place(x=0,y=0)
## create entry for username
my_entry_1=GUI.Entry()  
my_entry_1.place(x=0,y=20)
# ## creating label for password
label_2=GUI.Label(text="password")
label_2.place(x=0,y=40)
# ## create entry for password
my_entry_2=GUI.Entry(show="*")  
my_entry_2.place(x=0,y=60)

# ## creating button function 
def check():
    if my_entry_1.get().capitalize()=="Ahmed" and my_entry_2.get()=="1234":
        print("ok")
        main_window.destroy()

## creating ok button 
btn=GUI.Button(text="ok",command=check)
btn.place(x=150,y=59)

main_window.mainloop()