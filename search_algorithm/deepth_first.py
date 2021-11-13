from MiniScripts.CSVManip import getAdjDict
import random

def dfs(startCity,distCity):
    adj_list=getAdjDict()
    track_list = list()

    def dfs_algo(node):
        if (node not in track_list) :
            track_list.append(node)
            
            for neighbour in random.sample(adj_list[node].keys(),len(adj_list[node].keys())):
                if distCity == track_list[-1]:
                    break
                else:
                    dfs_algo(neighbour)
                    
    dfs_algo(startCity)
    #print(track_list)
    return track_list