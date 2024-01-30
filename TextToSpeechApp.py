from tkinter import *
from tkinter.ttk import *

root=Tk()

root.iconbitmap('icon.ico')
root.title("Text to Speech")

textArea=Text(root,height=20,width=90)
textArea.pack()

lblsp=Label(root, text ='Set the Speech Tempo',font = "50") 
lblsp.pack()
sp=Spinbox(root, from_= 100, to = 300) 
sp.pack()

def clickedRead():
    try:
        lblsp.config(text = "Speech Tempo")
        import pyttsx3  
        engine = pyttsx3.init()  
        voiceTempo=sp.get()
        engine.setProperty("rate", int(voiceTempo))

        text = textArea.get("1.0",END)  
        engine.say(text)    
        engine.runAndWait()  
        
    except:
        lblsp.config(text = "The Speech Tempo value is null!! Please set the value first!!")
        
import threading
readButton=Button(root,text = "Read",command=lambda: threading.Thread(target=clickedRead, daemon=True).start())
#readButton=Button(root,text = "Read",command=clickedRead)
readButton.pack()


def clickedCLR():
    textArea.delete("1.0","end")
    
clearButton=Button(root,text = "Clear All",command=clickedCLR)
clearButton.pack()

root.mainloop()