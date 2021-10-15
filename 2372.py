#2372 - Reunião
import sys 

vetor_distancia = []
class Graph(): 
  def __init__(self, vertices): 
    self.V = vertices 
    self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

  def minDistance(self, dist, sptSet): 
    min = sys.maxsize 
    for v in range(self.V): 
      if dist[v] < min and sptSet[v] == False: 
        min = dist[v] 
        min_index = v 
    return min_index 

  def dijkstra(self, src): 
    dist = [sys.maxsize] * self.V 
    dist[src] = 0
    sptSet = [False] * self.V 

    for _cout in range(self.V): 
      u = self.minDistance(dist, sptSet) 

      sptSet[u] = True

      for v in range(self.V): 
        if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
          dist[v] = dist[u] + self.graph[u][v]

    vetor_distancia.append(max(dist))

num_city, num_street = map(int, input().split())
g = Graph(num_city)
positions = range(num_city)
matrix = [[0] * num_city for i in positions]

for a in range(num_street):
  U, V, W = map(int, input().split())
  if (matrix[U][V] == 0 or matrix[U][V] > W):
    matrix[U][V] = W
    matrix[V][U] = W
g.graph = matrix
for city in range(num_city):
  g.dijkstra(city)

print(min(vetor_distancia))