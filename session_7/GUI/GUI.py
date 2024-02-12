import tkinter as GUI

def btn():
    pass
window=GUI.Tk()
window.title("Beta")
window.resizable(False,False)
window.geometry("400x400+100+100")
# window.configure(background="red")

selectevar=GUI.IntVar()

r1=GUI.Radiobutton(text="input",value=1,variable=selectevar,command=btn)
r1.place(x=0,y=0)
r2=GUI.Radiobutton(text="output",value=2,variable=selectevar,command=btn)
r2.place(x=100,y=0)

window.mainloop()