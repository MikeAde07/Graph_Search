
import queue


#User prompt for user to input file path, starting city, and destination

file_path = input('file path location: ')
start_node = input('starting city :')
goal_node = input('destination: ')


def uniform_cost_search(graph, start_node, goal_node=None) :
    """Uniform cost search function"""
    visited = set() # set keeps track of already visited/enclosed nodes
    q = queue.PriorityQueue() # Priority queue for uniform cost search (FRINGE). Sorts the Fringe based on g(n) values
    q.put((0, start_node, [start_node])) # Tuple (cummulative_cost, node, path)
    order = [] # nodes in UCS order
    solution_path = [] # solution path that will be updated once goal node is reached
    nodes_generated = 0
    nodes_popped = 0
    nodes_expanded = 0
    distance_traversed = 0

    while not q.empty() :  # while we have nodes to be processed into queue
        cummulative_cost, vertex, path = q.get()
        nodes_popped += 1
    

        if vertex not in visited :  # if it's the 1st time we visit this vertex
            nodes_expanded += 1
            order.append(vertex)
            visited.add(vertex)
            
    
        if vertex == goal_node : # If the goal node is reached
            solution_path = path
            break
        
        for neighbor, neighbor_cost in graph[vertex] : #go through all the neighbors of vertex and put them into the queue
                nodes_generated += 1
                if neighbor not in visited :
                    q.put((cummulative_cost + neighbor_cost, neighbor, path + [neighbor])) # Update path with the neighbor node
        distance_traversed += cummulative_cost # update distance traversed
    
# nodes generated, expanded, and popped
    print("Nodes generated:", nodes_generated)
    print("Nodes popped:", nodes_popped)
    print("Nodes expanded:", nodes_expanded)
    print("Distance traversed:", distance_traversed)
    print("Solution Path:", solution_path)

    return order, solution_path, distance_traversed



# Function to properly read in the input text file
def read_graph_from_file(file_path) :
  """Reads in the input.text file"""
  graph = {}
  with open(file_path, 'r') as file:
    for line in file :
      line = line.strip() # Remove leading and trailing whitespace
      if line == 'END OF INPUT' :
        break # Stop reading the file when 'END OF INPUT' is encountered
      if ' ' not in line :
        continue # Skip lines without spaces
      start_node, end_node, distance = line.split(' ')
      try :
        distance = int(distance) # Convert distance to integer
      except ValueError :
        print("Invalid distance value:", distance)
        continue
      #Adding the end node and its distance to the start node's neighbors
      if start_node not in graph:
          graph[start_node] = []
      graph[start_node].append((end_node, distance))
    # Adding the start node and its distance to the end node's neighbors
      if end_node not in graph :
          graph[end_node] = []
      graph[end_node].append((start_node, distance))
  return graph


graph = read_graph_from_file(file_path)

ucs_order = uniform_cost_search(graph, start_node, goal_node)
