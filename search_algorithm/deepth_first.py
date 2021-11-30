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

# run BFS multiple times and get shortest list
def pickBestDFS(startCity,distCity):
    REPEAT_LIMIT=20
    ouputList=list()
    for i in range(REPEAT_LIMIT):
        ouputList.append(dfs(startCity,distCity))
    ouputList.sort(key=len)
    # print("------------------")
    # print(startCity+" -> "+distCity)
    # print("------------------")
    # for output in ouputList:
    #     print(len(output),end=' : ')
    #     print(output)
    return ouputList[0]