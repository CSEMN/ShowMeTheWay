from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from MiniScripts import CSVManip
from MiniScripts.GeoCalculator import calc_pixels
from search_algorithm.a_star import a_star_search
from search_algorithm.breadth_first import bfs
from search_algorithm.deepth_first import dfs
import time
from threading import Thread

from search_algorithm.dijkstra import dijkstra
from search_algorithm.uniform_cost import uniformCostSearch


class UserEntryFrame(Frame):
    def __init__(self,master,pinPoint,drawArrow,clearMap):
        Frame.__init__(self, master)
        
        self.lblFrame=LabelFrame(master,text='User Entry')
        self.drawingColor='black'
        
        #circle all cities on the map
        #self.pinpointAllCities(pinPoint)
        
        self.algo = StringVar(self.lblFrame)
        self.algo.set("Uniform Cost") # default value

        self.algoSelector = ttk.OptionMenu(self.lblFrame, self.algo, "Uniform Cost","BFS", "DFS","A*","Dijkstra","Uniform Cost")
        self.algoSelector.grid(row=0,column=0,rowspan=2,padx=(10,5))
        self.isThreadRunning=False
        self.btn=ttk.Button(self.lblFrame,text='GO !!!',command=lambda :self.onClickAction(pinPoint,drawArrow))
        
        self.btn.grid(row=0,column=2,padx=(0,10))
        self.btnClear=ttk.Button(self.lblFrame,text='Clear',command=clearMap)
        self.btnClear.grid(row=1,column=2,padx=(0,10))
        self.btnStat()
        
       
        self.fromSelector = CitySelector(self.lblFrame,'From',None)
        self.fromSelector.grid(row=0,column=1,padx=(5,5),pady=(5,5))
        self.toSelector = CitySelector(self.lblFrame,'To     ',None)
        self.toSelector.grid(row=1,column=1,padx=(5,5),pady=(5,5))
        
        self.lblFrame.pack()

    def btnStat(self):
        if self.isThreadRunning:
            self.btn["state"] = DISABLED
            self.btnClear["state"] = DISABLED
        else:
            self.btn["state"] = NORMAL
            self.btnClear["state"] = NORMAL

    def onClickAction(self,pin_point,draw_arrow):

        #check if cities exists
        cityFrom=self.fromSelector.value.get()
        cityTo=self.toSelector.value.get()
        allCitiesList= CSVManip.getCitiesNamesList()
        
        if not cityFrom:#empty
            messagebox.showinfo("Empty Entry",'''Please, Enter "Start city" ''')
            return
        elif not cityTo:#empty
            messagebox.showinfo("Empty Entry",'''Please, Enter "Distnation city" ''')
            return
        elif cityFrom not in allCitiesList:
            messagebox.showerror("City Not Found",'''"Start City" isn't in dataset or misspelled ''')
            return
        elif cityTo not in allCitiesList:
            messagebox.showerror("City Not Found",'''"Distnation City" isn't in dataset or misspelled ''')
            return
        
        
        
        result=list()
        algoName=self.algo.get()
        if algoName=='BFS':
            result=bfs(cityFrom,cityTo)
            self.drawingColor='blue'
        elif algoName=='DFS':
            result=dfs(cityFrom,cityTo)
            self.drawingColor='red'
        elif algoName=='A*':
            result=a_star_search(cityFrom,cityTo)
            self.drawingColor='green'
        elif algoName=='Dijkstra':
            result=dijkstra(cityFrom,cityTo)
            self.drawingColor='brown'
        elif algoName=='Uniform Cost':
            result=uniformCostSearch(cityFrom,cityTo)
            self.drawingColor='purple'
        
        dataDict=CSVManip.dictCSVdata()

        def drawOnMap():
            self.isThreadRunning=True;
            self.btnStat()
            for index in range(0,len(result)):
                x=float(dataDict[result[index]]['lng'])
                y=float(dataDict[result[index]]['lat'])
                (x1,y1)=calc_pixels(x,y)
                pin_point(x1,y1,result[index],self.drawingColor)
                if index >0 :
                    x=float(dataDict[result[index-1]]['lng'])
                    y=float(dataDict[result[index-1]]['lat'])
                    (x0,y0)=calc_pixels(x,y)
                    draw_arrow(x0,y0,x1,y1,self.drawingColor)
                time.sleep(0.5)
            self.isThreadRunning=False;
            self.btnStat()
        thread = Thread(name='drawOnMapThread',target = drawOnMap)
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

