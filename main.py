from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    dist = {v: (float('inf'), float('inf')) for v in graph}
    dist[source] = (0, 0)

    # queue with distance, edge_count, and vertex
    queue = [(0, 0, source)]

    while queue:
        curr_dist, curr_edges, curr_node = heapq.heappop(queue)

        for v, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            new_edges = curr_edges + 1

            # check if we found a better path by updating to v
            if (new_dist < dist[v][0]) or (new_dist == dist[v][0] and new_edges < dist[v][1]):
                dist[v] = (new_dist, new_edges)
                heapq.heappush(queue, (new_dist, new_edges, v))

    # return the shortest path
    return dist
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    pass

