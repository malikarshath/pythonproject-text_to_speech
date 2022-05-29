from tkinter import *
from gtts import gTTS
from playsound import playsound

def text_to_speech():
    message = text.get()
    speech = gTTS(text = message)
    speech.save("speech.mp3")
    playsound("speech.mp3")
def exit():
    window.destroy()
def reset():
    text.set("")

window = Tk()
window.geometry('300x200')

window.title("TEXT TO SPEECH")

Label(window,text="TEXT TO SPEECH",font = "arial 15 bold").pack()

Label(window,text="ARSHA PROJECT",font = "arial 12 bold").pack(side='bottom')

Label(window,text="Enter Text",font = "arial 10 bold").place(x=10,y=40)

text = StringVar()
Entry(window,textvariable=text,width=40).place(x=10,y=70)

Button(window,text="PLAY",command=text_to_speech,font = "arial 10 bold").place(x=10,y=100)

Button(window,text="EXIT",command=exit,bg='red',font = "arial 10 bold").place(x=70,y=100)

Button(window,text="RESET",command=reset,font = "arial 10 bold").place(x=120,y=100)

window.mainloop()
