def bellman_ford(src, edgelist, V):
  dist = [float('inf')] * V
  dist[src] = 0

  # Relax all edges V-1 times
  for _ in range(V):
    # For each edge check if the distance from src
    # to vertex v including this edge is shorter
    # if it is update dist[v]
    for edge in edgelist:
      u, v, w = edge

      if dist[v] != float('inf'):
        dist[v] = min(dist[v], dist[u]+w)

  return dist
