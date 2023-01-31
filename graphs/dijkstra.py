import heapq
# graph is represented as an adjacency list
# {
#   0: [(1,3), (2,6)]
#   1: [(0,5), (3,2)]
#   ...
# }
def dijkstra(graph, src, V):
  dist = [float('inf')] * V
  dist[src] = 0

  h = [(0,src)]

  visited = set()
  visited.add(0)

  heapq.heapify(h)

  while len(h) > 0:
    weight, dest = heapq.heappop(h)
    visited.add(dest)

    dist[dest] = min(weight, dist[dest])

    for nei, nei_weight in graph[vertex]:
      if nei not in visited:
        heapq.heappush(h, (dist[vertex] + nei_weight, nei))

  return dist
