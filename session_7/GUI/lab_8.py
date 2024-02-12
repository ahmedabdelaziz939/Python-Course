import tkinter as GUI
main_window=GUI.Tk()
main_window.title("Welcome to Tkinter")
main_window.resizable(False,False)
main_window.geometry("300x300")



def btnaction():
    pass
y_shift=0
for i in range (8):
    label=GUI.Label(text=f"pin {i} mode",background="gray")
    label.place(x=0,y=y_shift)
    y_shift+=30
    
y_shift=0
for i in range (8):
    selectedBtn=GUI.IntVar()
    radio_1=GUI.Radiobutton(text="input",background="gray",value=i*2+1,variable=selectedBtn,command=btnaction)
    radio_1.place(x=100,y=y_shift)
   
    radio_2=GUI.Radiobutton(text="output",background="gray",value=2*i+2,variable=selectedBtn,command=btnaction)
    radio_2.place(x=150,y=y_shift)
    y_shift+=30
    





main_window.mainloop()        