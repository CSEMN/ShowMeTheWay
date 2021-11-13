from tkinter import *
from tkinter import ttk 
from MiniScripts import CSVManip
from MiniScripts.GeoCalculator import calc_pixels
from search_algorithm.a_star import a_star
from search_algorithm.breadth_first import bfs
from search_algorithm.deepth_first import dfs
import time
from threading import Thread


class UserEntryFrame(Frame):
    def __init__(self,master,pinPoint,drawArrow,clearMap):
        Frame.__init__(self, master)
        
        self.lblFrame=LabelFrame(master,text='User Entry')
        
        #circle all cities on the map
        #self.pinpointAllCities(onClick)
        
        self.algo = StringVar(self.lblFrame)
        self.algo.set("BFS") # default value

        self.algoSelector = ttk.OptionMenu(self.lblFrame, self.algo, "BFS","BFS", "DFS")
        self.algoSelector.grid(row=0,column=0,rowspan=2,padx=(10,5))
        self.isThreadRunning=False
        self.btn=ttk.Button(self.lblFrame,text='GO !!!',command=lambda :self.onClickAction(pinPoint,drawArrow,clearMap))
        self.btnStat()
        self.btn.grid(row=0,column=2,rowspan=2,padx=(0,10))
        
       
        self.fromSelector = CitySelector(self.lblFrame,'From',None)
        self.fromSelector.grid(row=0,column=1,padx=(5,5),pady=(5,5))
        self.toSelector = CitySelector(self.lblFrame,'To     ',None)
        self.toSelector.grid(row=1,column=1,padx=(5,5),pady=(5,5))
        
        self.lblFrame.pack()

    def btnStat(self):
        if self.isThreadRunning:
            self.btn["state"] = DISABLED
        else:
            self.btn["state"] = NORMAL

    def onClickAction(self,pin_point,draw_arrow,clearMap):
        # x=float(self.xposEntry.get())
        # y=float(self.yposEntry.get())
        # func(x,y,'Click !')
        clearMap()
        cityFrom=self.fromSelector.value.get()
        cityTo=self.toSelector.value.get()
        result=list()
        algoName=self.algo.get()
        if algoName=='BFS':
            result=bfs(cityFrom,cityTo)
        elif algoName=='DFS':
            result=dfs(cityFrom,cityTo)
        elif algoName=='A*':
            result=a_star(cityFrom,cityTo)
        
        dataDict=CSVManip.dictCSVdata()

        def drawOnMap():
            self.isThreadRunning=True;
            self.btnStat()
            for index in range(0,len(result)):
                x=float(dataDict[result[index]]['lng'])
                y=float(dataDict[result[index]]['lat'])
                (x1,y1)=calc_pixels(x,y)
                pin_point(x1,y1,result[index])
                if index >0 :
                    x=float(dataDict[result[index-1]]['lng'])
                    y=float(dataDict[result[index-1]]['lat'])
                    (x0,y0)=calc_pixels(x,y)
                    draw_arrow(x0,y0,x1,y1)
                time.sleep(0.5)
            self.isThreadRunning=False;
            self.btnStat()
        thread = Thread(name='drawOnMapThread',target = drawOnMap)
        if not thread.is_alive():
            thread.start()

            




    
    def pinpointAllCities(self,func):
        data=CSVManip.getCSVData()
        for city in data:
            x=float(city['lng'])
            y=float(city['lat'])
            (xpos,ypos)=calc_pixels(x,y)
            func(xpos,ypos,city['city'])

        

class CitySelector(Frame):
    def __init__(self,master,title,onSelect):
        Frame.__init__(self, master)
        cities_list= CSVManip.getCitiesNamesList()
        
        self.lbl=Label(self,text=title)
        self.lbl.pack(side=LEFT)
        self.value=StringVar()
        self.cmbBox=ttk.Combobox(self,values=cities_list,textvariable=self.value)
        self.cmbBox.pack(side=RIGHT)

