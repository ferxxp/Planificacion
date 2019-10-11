import tkinter as tk



def dumpMap(charMap):
    for line in charMap:
        print(line)

def StartDisplayMap(charMap):
    app = tk.Tk()
    app.title("Map progress")
    Fprint=tk.Frame(app)
    label = tk.Label(app,text=str(charMap).replace('\'','').replace(']','\n').replace('[','').replace(',','').replace('0',' '))
    return [app,Fprint,label]
def updateDisplay(charMap,app,Fprint,label):
    label.config(text=str(charMap).replace('\'','').replace(']','\n').replace('[','').replace(',','').replace('2','X').replace('0','  '))
    label.pack()
    app.update_idletasks()
    app.update()
