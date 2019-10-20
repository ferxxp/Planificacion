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
def StartDisplayclean(charMap):
    app = tk.Tk()
    app.title("Map progress")
    Fprint=tk.Frame(app)
    l=0
    for line in charMap:
        c=0
        for char in line:
            if char=='1':
                label = tk.Label(app,text=str(char),bg="black")
                label.grid(row=l,column=c)
            elif char=='0' :
                label = tk.Label(app,text=" ")
                label.grid(row=l,column=c)
            elif char=='4' :
                label = tk.Label(app,text=" ",bg="green")
                label.grid(row=l,column=c)
            elif char=='3'or chr=='2':
                label = tk.Label(app,text=" ",bg="blue")
                label.grid(row=l,column=c)
            c=c+1
        l=l+1
    app.update_idletasks()
    app.update()
    return [app,Fprint,label]
def updateDisplayclean(charMap,app,Fprint):
    l=0
    for line in charMap:
        c=0
        for char in line:
            if char =='2':
                a=app.grid_slaves(l,c)[0]
                a.config(bg='orange')
            c=c+1
        l=l+1
    app.update_idletasks()
    app.update()
def addsolutionclean(app,nodes):
    for node in nodes:
        a=app.grid_slaves(node.x,node.y)[0]
        a.config(bg='red')
    app.update_idletasks()
    app.update()
