# Using adjacency list
#
# Approach 1
# - Empties queue at each level
# - Reassigns queue as the next level
# This is useful for Trees where we need distinction on levels
def bfs(self, vertex, graph):
  visited = {}

  queue = [vertex]
  visited[vertex] = True

  # Level by level traversal
  while len(queue) > 0:
    next_level = []

    for node in queue:
      print(node)
      for nei in graph[node]:
        if nei not in visited:
          next_level.append(nei)
          visited[nei] = True

      queue = next_level

# Approach 2
# Queue is popped while the nodes are appended
def bfs(self, size, graph):
  visited = [False]*size

  def traverse(node):
    queue = [node]
    visited[node] = True

    while len(queue) > 0:
      curr = queue.pop(0)

      print(curr)

      for nei in graph[curr]:
        if not visited[nei]:
          visited[curr] = True
          queue.append(nei)

  # Try BFS for all nodes, this ensures nodes
  # which are not connected to the graph are
  # also explored.
  for node in range(size):
    if not visited[node]:
      visited[node] = True
      traverse(node)
