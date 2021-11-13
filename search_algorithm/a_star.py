
from MiniScripts.CSVManip import dictCSVdata, getAdjDict


def a_star(startCity,distCity):
    adj_list=getAdjDict()
    data=dictCSVdata()
    track_list = list()
    

    def a_star_algo(current):
        track_list.append(current)
        if current== distCity:
            return
        distances_dict=dict()
        for adjCity in adj_list[current].keys():
            distances_dict[adjCity]=data[adjCity][distCity]

        #distances_dict=dict(sorted(distances_dict.items(), key=lambda item: item[1]))#lowest distance first
        #city,distance=min(distances_dict.items(), key=lambda x: x[1]) 
        nearestCity=sorted(distances_dict.items(), key=lambda item: item[1])[0][0]
        a_star_algo(nearestCity)
    
    a_star_algo(startCity)
    return track_list

    # def retracePath(c):
    #     path.insert(0,c)
    #     if c.parent == None:
    #         return
    #     retracePath(c.parent)

    # openList.append(current)
    # while len(openList) is not 0:
    #     current = min(openList, key=lambda inst:inst.H)
    #     if current == end:
    #         return retracePath(current)
    #     openList.remove(current)
    #     closedList.append(current)
    #     for tile in graph[current]:
    #         if tile not in closedList:
    #             tile.H = (abs(end.x-tile.x)+abs(end.y-tile.y))*10 
    #             if tile not in openList:
    #                 openList.append(tile)
    #             tile.parent = current
    # return path