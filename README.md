# DAA-Lab-2024

Solutions of weekly coding assignments/ labs for the course *Design and Analysis of Algorithms* (DAA) *Lab* conducted by prof [Apurba Das](https://sites.google.com/site/apurbadas348math/home) and prof [Sourav Mukhopadhyay](http://www.facweb.iitkgp.ac.in/~sourav/) of **IIT Kharagpur Maths department** held at Takshashila CIC for the session Autumn 2024-25.

```
# Define a function to implement Dijkstra's algorithm
def dijkstra(n, edges, start, distanceThreshold):
    # Initialize distances as infinity and set the start city distance to 0
    dist = [float('inf')] * n
    dist[start] = 0
    # Track visited cities
    visited = [False] * n
    
    for _ in range(n):
        # Find the unvisited city with the smallest distance
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == float('inf'):
            break
        
        # Mark the city as visited
        visited[u] = True
        
        # Update distances for neighboring cities
        for edge in edges:
            if edge[0] == u or edge[1] == u:
                v = edge[1] if edge[0] == u else edge[0]
                weight = edge[2]
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    # Count cities within the distance threshold
    reachable_cities = sum(1 for d in dist if d <= distanceThreshold and d != float('inf'))
    return reachable_cities

# Main function to find the city with the smallest number of reachable cities
def findTheCity(n, edges, distanceThreshold):
    min_reachable = float('inf')
    result_city = -1

    for city in range(n):
        reachable = dijkstra(n, edges, city, distanceThreshold)
        if reachable < min_reachable or (reachable == min_reachable and city > result_city):
            min_reachable = reachable
            result_city = city

    return result_city

# Input values
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4

# Find the city with the smallest number of reachable cities
output = findTheCity(n, edges, distanceThreshold)
print("Output:", output)
