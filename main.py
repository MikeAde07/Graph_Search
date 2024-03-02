
import queue

#User prompt for user to input file path, starting city, and destination

file_path = input('file path location: ')
start_node = input('starting city :')
goal_node = input('destination: ')

def order_bfs(graph, start_node, goal_node=None) :
  """Breadth-First Search function"""

  visited = set() # set keeps track of already visited nodes
  q = queue.Queue() # FIFO queue
  q.put((start_node, 0)) # Tuple (node, distance)
  order = [] # nodes in BFS order
  nodes_generated = 0
  nodes_popped = 0
  nodes_expanded = 0
  distance_traversed = 0

  while not q.empty() :  # while we have nodes to be processed into queue
    vertex_tuple = q.get() # node and its distance from the start node
    vertex = vertex_tuple[0]
    dist = vertex_tuple[1]
    nodes_popped += 1

    if vertex not in visited :  # if it's the 1st time we visit this vertex
      order.append(vertex)
      visited.add(vertex)
      if isinstance(dist, int): # Check if the distance is already an integer
        distance_traversed += dist
      if vertex == goal_node : # If the goal node is reached
        break
      nodes_expanded += 1
      for neighbor, neighbor_dist in graph[vertex] : #go through all the neighbors of vertex and put them into the queue
            nodes_generated += 1
            if neighbor not in visited :
                q.put((neighbor, neighbor_dist + int(dist))) # Add the neighbor


  print("Nodes generated:", nodes_generated)
  print("Nodes popped:", nodes_popped)
  print("Nodes expanded:", nodes_expanded)
  print("Distance traversed:", distance_traversed)

  return order

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
      graph[start_node].append((end_node, distance)) # previously "graph[start_node][end_node] = int(distance)""
    # Adding the start node and its distance to the end node's neighbors
      if end_node not in graph :
          graph[end_node] = []
      graph[end_node].append((start_node, distance)) # previously "graph[end_node][start_node] = int(distance)""
  return graph


graph = read_graph_from_file(file_path)

bfs_order = order_bfs(graph, start_node, goal_node)
print("BFS Traversal Order:", bfs_order)
