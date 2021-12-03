from MiniScripts.CSVManip import dictCSVdata, getAdjDict
from queue import PriorityQueue

def uniformCostSearch(startCity, distCity):
    adj_list=getAdjDict()
    data=dictCSVdata()
    visited = set()                  # set of visited nodes
    visited.add(startCity)                   # mark the starting vertex as visited
    q = PriorityQueue()        # we store vertices in the (priority) queue as tuples with cumulative cost
    q.put((0, startCity))                    # add the starting node, this has zero *cumulative* cost   
    goal_node = distCity                 # this will be set as the goal node if one is found
    parents = {startCity:None}               # this dictionary contains the parent of each node, necessary for path construction

    while not q.empty():             # while the queue is nonempty
        dequeued_item = q.get()        
        current_node = dequeued_item[1]             # get node at top of queue
        current_node_priority = dequeued_item[0]    # get the cumulative priority for later

        if current_node == goal_node:                    # if the current node is the goal
            path_to_goal = [current_node]           # the path to the goal ends with the current node (obviously)
            prev_node = current_node                # set the previous node to be the current node (this will changed with each iteration)

            while prev_node != startCity:                   # go back up the path using parents, and add to path
                parent = parents[prev_node]
                path_to_goal.append(parent)   
                prev_node = parent
                
            path_to_goal.reverse()                  # reverse the path
            return path_to_goal                     # return it

        else:
            for adjCity in adj_list[current_node].keys():     # otherwise, for each adjacent node
                child = adjCity                 # (avoid calling .to() in future)

                if child not in visited:            # if it is not visited
                    visited.add(child)              # mark it as visited
                    parents[child] = current_node   # set the current node as the parent of child
                    q.put((current_node_priority + float(data[current_node][child+"_r"]), child)) # and enqueue it with *cumulative* priority