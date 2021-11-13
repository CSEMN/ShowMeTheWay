from queue import Queue
from  MiniScripts.CSVManip import getAdjDict
import random

def bfs(startCity,distCity):
    adj_list=getAdjDict()
    #print(adj_list)
    #bsf code
    visited={}
    level={}
    parent={}
    bfs_traversal_output=[]
    queue=Queue()
    #initail values
    for node in adj_list.keys():
        visited[node]=False
        parent[node]=None
        level[node]=-1

    start=startCity
    visited[start]=True
    level[start]=0
    queue.put(start)
    while not queue.empty():
        u=queue.get()
        bfs_traversal_output.append(u)
        if u==distCity:
            break;

        for v in random.sample(adj_list[u].keys(),len(adj_list[u].keys())):
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                level[v]=level[u]+1
                queue.put(v)
    #if not found redo the algorithm
    while(bfs_traversal_output[-1]!=distCity):
        bfs_traversal_output=bfs(startCity,distCity)
    return bfs_traversal_output

