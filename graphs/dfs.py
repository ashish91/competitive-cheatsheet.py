# Using adjacency list
def dfs(self, vertex, graph):
	visited = {}

	def recursive(v):
		print(v)
		neighbours = graph[v]

		for node in neighbours:
			if node not in visited:
				visited[node] = True
				recursive(node)

	recursive(vertex)
