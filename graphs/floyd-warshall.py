def floyd_warshall(mat):
  V = len(mat)
  dist = [[float('inf') for v in range(V)] for u in range(V)]

  for u in range(V):
    for v in range(V):
      dist[u][v] = mat[u][v]

  for u in range(V):
    for v in range(V):
      for intermediate in range(V):
        dist[u][v] = min(dist[u][v], dist[u][intermediate] + dist[intermediate][v])

  return dist
