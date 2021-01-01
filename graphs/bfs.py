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
      for neighbour in graph[node]:
        if neighbour not in visited:
          next_level.append(neighbour)
          visited[neighbour] = True

      queue = next_level

# Approach 2
# Queue is popped while the nodes are appended
def bfs(self, vertex, graph):
  visited = {}

  queue = [vertex]
  visited[vertex] = True

  # Level by level traversal
  while len(queue) > 0:
    current = queue.pop(0)

    print(current)

    for neighbour in graph[current]:
      if neighbour not in visited:
        queue.append(neighbour)
        visited[current] = True
