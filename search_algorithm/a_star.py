
from MiniScripts.CSVManip import dictCSVdata, getAdjDict
from queue import PriorityQueue


def a_star_search(startCity, distCity):
    adj_list=getAdjDict()
    data=dictCSVdata()
    frontier = PriorityQueue()
    frontier.put(startCity, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[startCity] = None
    cost_so_far[startCity] = 0.0
    
    while not frontier.empty():

        current = frontier.get()
        if current == distCity:
            break
        
        for next in adj_list[current]:
            new_cost = cost_so_far[current] + float(data[current][next+"_r"])
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost +  float(data[next][distCity])
                frontier.put(next, priority)
                came_from[next] = current
    
    path=list()
    path.append(distCity)
    while(came_from[path[-1]]!=None):
        path.append(came_from[path[-1]])
    
    path.reverse() 
    return path
