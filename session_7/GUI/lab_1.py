import tkinter as GUI
main_window=GUI.Tk()

### how to set title
main_window.title("Welcome to Tkinter")
### how to make it not resizable resizable
main_window.resizable(False,False)
### how to set geometry
main_window.geometry("400x100")

main_window.mainloop()