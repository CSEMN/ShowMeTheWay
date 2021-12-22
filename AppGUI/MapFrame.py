from tkinter import *
from PIL import ImageTk,Image

class MapFrame(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master=master
        self.drawingList=[]

        self.im = Image.open("assets/the_map.png").resize((800,500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.im)
        self.mapCanvas = Canvas(self.master,width=800,height=500)
        self.mapCanvas.create_image(0,0,image=self.photo,anchor="nw")
        self.mapCanvas.pack(fill='both',anchor='nw')
        
    
    def drawPoint(self,x,y,label,color):  
        #self.resetCanvas()
        r=3
        self.drawingList.append(self.mapCanvas.create_oval(x-r,y-r,x+r,y+r,fill=color))
        r=5
        self.drawingList.append(self.mapCanvas.create_oval(x-r,y-r,x+r,y+r,outline=color))
        self.drawingList.append(self.mapCanvas.create_text(x,y-10,text=label))
        
    
    def drawLine(self,x0,y0,x1,y1,color):      
        self.drawingList.append(self.mapCanvas.create_line(x0,y0,x1,y1,fill=color,width=2.5,arrow=LAST))

    def resetCanvas(self):
        for item in self.drawingList:
            self.mapCanvas.delete(item);
        self.drawingList.clear()
        



        

