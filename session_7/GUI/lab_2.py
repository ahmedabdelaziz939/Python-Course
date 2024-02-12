import tkinter as GUI
main_window=GUI.Tk()
main_window.title("Welcome to Tkinter")
main_window.resizable(False,False)
main_window.geometry("400x400")

for i in range(5):
    ## creating button
    btn=GUI.Button(text=f"Button {i}")
    ## dispalying button
    btn.pack() 




main_window.mainloop()