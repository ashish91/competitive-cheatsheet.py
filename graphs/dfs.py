# Using adjacency list
def dfs(self, size, graph):
  visited = [False]*size

  # Recursively explore unvisited neighbors
  # of the node.
  def recursion(node):
    neighbours = graph[node]

    for nei in neighbours:
      if not visited[nei]:
        visited[nei] = True
        recursion(nei)

  # Try DFS for all nodes, this ensures nodes
  # which are not connected to the graph are
  # also explored.
  for node in range(size):
    if not visited[node]:
      visited[node] = True
      recursion(node)
