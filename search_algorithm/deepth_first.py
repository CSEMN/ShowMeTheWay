from MiniScripts.CSVManip import getAdjDict

def dfs(startCity,distCity):
    adj_list=getAdjDict()
    track_list = list()
    parent=dict()
    parent[startCity]= None

    def dfs_algo(node):
        
        if (node not in track_list) :
            track_list.append(node)
            
            for neighbour in adj_list[node].keys():
                if distCity == track_list[-1]:
                    break
                elif neighbour not in track_list:
                    parent[neighbour]=node
                    dfs_algo(neighbour)
                
    dfs_algo(startCity)
    path=list()
    node=distCity;

    while( node != startCity):
        path.append(node)
        node=parent[node]
    path.append(startCity)
    path.reverse()
    return path
