from MiniScripts.CSVManip import dictCSVdata, getAdjDict
from queue import PriorityQueue

def uniformCostSearch(startCity, distCity):
    adj_list=getAdjDict()
    data=dictCSVdata()
    visited = set()                 
    visited.add(startCity)               
    q = PriorityQueue()       
    q.put((0, startCity))              
    goal_node = distCity              
    parents = {startCity:None}              

    while not q.empty():            
        dequeued_item = q.get()        
        current_node = dequeued_item[1]           
        current_node_priority = dequeued_item[0]   

        if current_node == goal_node:                   
            path_to_goal = [current_node]          
            prev_node = current_node               

            while prev_node != startCity:                 
                parent = parents[prev_node]
                path_to_goal.append(parent)   
                prev_node = parent
                
            path_to_goal.reverse()                 
            return path_to_goal                   

        else:
            for adjCity in adj_list[current_node].keys():     
                child = adjCity                

                if child not in visited:            
                    visited.add(child)              
                    parents[child] = current_node   
                    q.put((current_node_priority + float(data[current_node][child+"_r"]), child)) 