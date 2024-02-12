import tkinter as GUI
import math
main_window=GUI.Tk()
main_window.title("Welcome to Tkinter")
main_window.resizable(False,False)
main_window.geometry("450x450")


for i in range(3): 
    for j in range(3):
       if (i==0 and j==0) or(i==0 and j==2) or (i==2 and j==0) or(i==2 and j==2) or(i==1 and j==1) :
           continue
       else:
           ## creating button
           btn=GUI.Button(text="OK",width=math.floor(20))
           main_window.grid_columnconfigure(3,minsize=50)
           main_window.grid_rowconfigure(3,minsize=80)
           ## dispalying button
           btn.grid(row=j,column=i) 
           
main_window.mainloop()