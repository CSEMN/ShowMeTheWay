from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk,Image
from AppGUI import MapFrame,UserEntryFrame



class MainWindow:
    def __init__(self,root:Tk):
        
        self.configWindow(root)
        self.mpFrame=MapFrame.MapFrame(root)
        self.uef=UserEntryFrame.UserEntryFrame(root,self.mpFrame.drawPoint,self.mpFrame.drawLine,self.mpFrame.resetCanvas)
        self.img = Image.open("assets/info.png").resize((20,20), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)
        ttk.Button(root,image=self.photo,command=lambda :self.showCriedts(root)).place(x=770,y=0)
        self.uef.pack(anchor='n',pady=(10,10))
        self.mpFrame.pack(fill='both',anchor='nw')


    def configWindow(self,window:Tk):
        window.title("ShowMeTheWay")
        window.geometry('800x600')
        window.resizable(0,0);

    def showCriedts(self,master):
        window=Toplevel(master)
        boldfont=font.Font(weight="bold",size=20)
        Label(window,text='Coded By').pack()
        Label(window,text='Mahmoud Nasser',font=boldfont).pack()
        Label(window,text='Supervised by').pack()
        Label(window,text='Dr\\ Ahmed Ghozia',font=boldfont).pack()
        
        
    
if __name__=='__main__':
    root=Tk()
    MainWindow(root)
    root.mainloop()