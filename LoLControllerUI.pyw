import tkinter
import keyboard
import pyperclip
import pystray
from PIL import Image

entryText_1 = ""
entryText_2 = ""
entryText_3 = ""
entryText_4 = ""
entryText_5 = ""

def updateEntries():
    global entryText_1, entryText_2, entryText_3, entryText_4, entryText_5
    entryText_1 = entry_1.get()
    entryText_2 = entry_2.get()
    entryText_3 = entry_3.get()
    entryText_4 = entry_4.get()
    entryText_5 = entry_5.get()

def copy_1():
    pyperclip.copy(entryText_1)    

def copy_2():
    pyperclip.copy(entryText_2)

def copy_3():
    pyperclip.copy(entryText_3)
    
def copy_4():
    pyperclip.copy(entryText_4)
    
def copy_5():
    pyperclip.copy(entryText_5)

keyboard.add_hotkey('f20', copy_1)
keyboard.add_hotkey('f21', copy_2)
keyboard.add_hotkey('f22', copy_3)
keyboard.add_hotkey('f23', copy_4)
keyboard.add_hotkey('f24', copy_5)

def quit_window(icon, item):
    icon.stop()
    window.destroy()
    
def show_window(icon, item):
    icon.stop()
    window.deiconify()

# Hide the window and show on the system taskbar
def hide_window():
    updateEntries()
    window.withdraw()
    image=Image.open("favicon.ico")
    menu=pystray.Menu(pystray.MenuItem('LoL Controller', show_window, default=True))
    icon=pystray.Icon("name", image, "LoL Controller", menu)
    icon.run()

#User Interface
window = tkinter.Tk()
window.iconbitmap("favicon.ico")
window.title("LoL Controller")
window.resizable(False, False)

label_1 = tkinter.Label(window, text="Button TOP")
label_1.grid(row=0, column=0, padx='5', pady='5')
entry_1 = tkinter.Entry(window, width=30)
entry_1.grid(row=0, column=1, padx='5', pady='5')
entry_1.insert(0, "TOP")

label_2 = tkinter.Label(window, text="Button JUNGLE")
label_2.grid(row=1, column=0, padx='5', pady='5')
entry_2 = tkinter.Entry(window, width=30)
entry_2.grid(row=1, column=1, padx='5', pady='5')
entry_2.insert(0, "JUNGLE")

label_3 = tkinter.Label(window, text="Button MID")
label_3.grid(row=2, column=0, padx='5', pady='5')
entry_3 = tkinter.Entry(window, width=30)
entry_3.grid(row=2, column=1, padx='5', pady='5')
entry_3.insert(0, "MID")

label_4 = tkinter.Label(window, text="Button SUPPORT")
label_4.grid(row=3, column=0, padx='5', pady='5')
entry_4 = tkinter.Entry(window, width=30)
entry_4.grid(row=3, column=1, padx='5', pady='5')
entry_4.insert(0, "SUPPORT")

label_5 = tkinter.Label(window, text="Button BOT")
label_5.grid(row=4, column=0, padx='5', pady='5')
entry_5 = tkinter.Entry(window, width=30)
entry_5.grid(row=4, column=1, padx='5', pady='5')
entry_5.insert(0, "BOT")

btnOk = tkinter.Button(window, text="OK", width=20, command=hide_window)
btnOk.grid(row=5, column=0, columnspan=2, pady='10')

window.mainloop()