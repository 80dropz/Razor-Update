import customtkinter
import tkinter
import time
import keyboard
main = tkinter.Tk()
main.geometry("500x350")
main.title("Dropz Razor Update")
i = 0
#chroma should work my mac cant run it :sob:
#chroma should work my mac cant run it :sob:

def overlap():
    if keyboard.KEY_DOWN == Key1:
        print("key 1 was pressed")
        keyboard.KEY_UP(key2, key3, key4, Key1)
        time.sleep(0.0001)
        keyboard.KEY_DOWN(Key1)
    elif keyboard.KEY_DOWN == key2:
        keyboard.KEY_UP(Key1, key3, key4, key2)
        time.sleep(0.0001)
        keyboard.KEY_DOWN(key2)
    elif keyboard.KEY_DOWN == key3:
        keyboard.KEY_UP(Key1, key2, key4, key3)
        time.sleep(0.0001)
        keyboard.KEY_DOWN(key3)
    elif keyboard.KEY_DOWN == key4:
        keyboard.KEY_UP(Key1, key2, key3, key4)
        time.sleep(0.0001)
        keyboard.KEY_DOWN(key4)


def runningtxt():
    while running.get() == 1:
        overlap()
    if running.get() == 1:
        runninglbl.configure(text="Running! ✅", text_color="Green")
    elif running.get() == 0:
        runninglbl.configure(text="Not Running 🔴", text_color="red")
def quit():
    main.destroy()
def chroma():
    while i < 100:
        Header.configure(text_color="Red")
        time.sleep(.5)
        Header.configure(text_color="Blue")
        time.sleep(.5)
        Header.configure(text_color="Light blue")
        time.sleep(.5)
        Header.configure(text_color="Dark green")
        time.sleep(.5)
        Header.configure(text_color="light green")
        time.sleep(.5)
#chroma should work my mac cant run it :sob:
def printkeys():
    keyslbl.configure(text="Your keybinds are: " + Key1.get() +", "+ key2.get() +", "+ key3.get() +", "+ key4.get(), text_color="Light Grey")
Header = customtkinter.CTkLabel(main, text="No Overlap", font=("Roboto", 36))
Header.place(relx=.5, rely=.1, anchor=tkinter.CENTER)
semiheader = customtkinter.CTkLabel(main, text="By @80dropz", font=("roboto", 10))
semiheader.place(relx=.5, rely=.2, anchor=tkinter.CENTER)
quitbtn = customtkinter.CTkButton(main, text="Quit", width=30, height=15, corner_radius=10, command=quit)
quitbtn.place(relx=.045, rely=.025, anchor=tkinter.CENTER)
keylbl = customtkinter.CTkLabel(main, text="Enter your keys", font=("roboto", 24))
keylbl.place(relx=.5, rely=.3, anchor=tkinter.CENTER)
Key1 = customtkinter.CTkEntry(main, placeholder_text="Key 1", width=75)
Key1.place(relx=.2, rely=.4, anchor=tkinter.CENTER)
key2 = customtkinter.CTkEntry(main, placeholder_text="Key 2", width=75)
key2.place(relx=.4, rely=.4, anchor=tkinter.CENTER)
key3 = customtkinter.CTkEntry(main, placeholder_text="Key 3", width=75)
key3.place(relx=.6, rely=.4, anchor=tkinter.CENTER)
key4 = customtkinter.CTkEntry(main, placeholder_text="Key 4", width=75)
key4.place(relx=.8, rely=.4, anchor=tkinter.CENTER)
Donebtn = customtkinter.CTkButton(main, text="Done", fg_color="green", corner_radius=10, command=printkeys)
Donebtn.place(relx=.3, rely=.5,  anchor=tkinter.CENTER)
running = customtkinter.CTkCheckBox(main, text="Run", command=runningtxt)
running.place(relx=.6, rely=.5, anchor=tkinter.CENTER)
keyslbl = customtkinter.CTkLabel(main, text="", font=("Roboto", 24))
keyslbl.place(relx=.5, rely=.6, anchor=tkinter.CENTER)
runninglbl = customtkinter.CTkLabel(main, text="Not Running", font=("Roboto", 24))
runninglbl.place(relx=.5, rely=.7, anchor=tkinter.CENTER)

#chroma should work my mac cant run it :sob:
#chroma should work my mac cant run it :sob:
#chroma should work my mac cant run it :sob:
#chroma should work my mac cant run it :sob:
#chroma should work my mac cant run it :sob:
main.mainloop()
