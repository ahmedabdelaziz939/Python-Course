import tkinter as GUI
main_window=GUI.Tk()
main_window.title("Welcome to Tkinter")
main_window.resizable(False,False)
main_window.geometry("300x300")

selectedBtn=GUI.IntVar()
# selectedBtn2=GUI.IntVar()
# selectedBtn3=GUI.IntVar()
# selectedBtn4=GUI.IntVar()
# selectedBtn5=GUI.IntVar()
# selectedBtn6=GUI.IntVar()
# selectedBtn7=GUI.IntVar()
# selectedBtn8=GUI.IntVar()

def btnaction():
   pass

y_shift=0
# for i in range (8):
#     label=GUI.Label(text=f"pin {i} mode",background="gray")
#     label.place(x=0,y=y_shift)
#     y_shift+=30
    
y_shift=0
radio_1=GUI.Radiobutton(text="input",background="gray",value=1,variable=selectedBtn,command=btnaction)
radio_1.place(x=100,y=y_shift)

radio_2=GUI.Radiobutton(text="output",background="gray",value=2,variable=selectedBtn,command=btnaction)
radio_2.place(x=150,y=y_shift)
y_shift+=30

# radio_3=GUI.Radiobutton(text="input",background="gray",value=3,variable=selectedBtn2,command=btnaction)
# radio_3.place(x=100,y=y_shift)

# radio_4=GUI.Radiobutton(text="output",background="gray",value=4,variable=selectedBtn2,command=btnaction)
# radio_4.place(x=150,y=y_shift)
# y_shift+=30

# radio_5=GUI.Radiobutton(text="input",background="gray",value=3,variable=selectedBtn3,command=btnaction)
# radio_5.place(x=100,y=y_shift)

# radio_6=GUI.Radiobutton(text="output",background="gray",value=4,variable=selectedBtn3,command=btnaction)
# radio_6.place(x=150,y=y_shift)
# y_shift+=30

# radio_7=GUI.Radiobutton(text="input",background="gray",value=3,variable=selectedBtn4,command=btnaction)
# radio_7.place(x=100,y=y_shift)

# radio_8=GUI.Radiobutton(text="output",background="gray",value=4,variable=selectedBtn4,command=btnaction)
# radio_8.place(x=150,y=y_shift)
# y_shift+=30

# radio_9=GUI.Radiobutton(text="input",background="gray",value=3,variable=selectedBtn5,command=btnaction)
# radio_9.place(x=100,y=y_shift)

# radio_10=GUI.Radiobutton(text="output",background="gray",value=4,variable=selectedBtn5,command=btnaction)
# radio_10.place(x=150,y=y_shift)
# y_shift+=30

# radio_11=GUI.Radiobutton(text="input",background="gray",value=3,variable=selectedBtn6,command=btnaction)
# radio_11.place(x=100,y=y_shift)

# radio_12=GUI.Radiobutton(text="output",background="gray",value=4,variable=selectedBtn6,command=btnaction)
# radio_12.place(x=150,y=y_shift)
# y_shift+=30

# radio_13=GUI.Radiobutton(text="input",background="gray",value=3,variable=selectedBtn7,command=btnaction)
# radio_13.place(x=100,y=y_shift)

# radio_14=GUI.Radiobutton(text="output",background="gray",value=4,variable=selectedBtn7,command=btnaction)
# radio_14.place(x=150,y=y_shift)
# y_shift+=30

# radio_15=GUI.Radiobutton(text="input",background="gray",value=3,variable=selectedBtn8,command=btnaction)
# radio_15.place(x=100,y=y_shift)

# radio_16=GUI.Radiobutton(text="output",background="gray",value=4,variable=selectedBtn8,command=btnaction)
# radio_16.place(x=150,y=y_shift)
# y_shift+=30

main_window.mainloop()        