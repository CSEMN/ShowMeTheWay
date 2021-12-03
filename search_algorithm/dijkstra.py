from MiniScripts.CSVManip import dictCSVdata, getAdjDict,getCitiesNamesList
from queue import PriorityQueue

def dijkstra(startCity,distCity):

    adj_list=getAdjDict()
    data=dictCSVdata()
    allCities=getCitiesNamesList()
    Q=PriorityQueue()
    distances = dict()
    prev = dict()
    found =False
    #Initialize data
    Q.put(startCity,0.0)
    for city in allCities:
        distances[city]=float('inf')#infinity
        prev[city]=None
    distances[startCity]=0.0
    while Q.not_empty:
        if  prev[distCity]!=None:
            found =True
            break
        node = Q.get()
        for adjCity in adj_list[node]:
            newdistance= distances[node]+float(data[node][adjCity+"_r"])
            if newdistance < distances[adjCity] :
                distances[adjCity]=newdistance
                prev[adjCity]=node
                Q.put(adjCity,newdistance)
    if found:
        path=list()
        node=distCity
        if prev[node] != None or node==startCity:
            while node != None :
                path.append(node)
                node=prev[node]
        path.reverse()
        return path
    else:
        raise AttributeError("distination city not found by Dijkstra algorithm") 
    


