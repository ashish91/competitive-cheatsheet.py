class Heap:
	def __init__(self, size):
		self.size = 0
		self.maxsize = maxsize
		self.mem = [0] * (self.maxsize + 1)
		self.mem[0] = float('inf')
		self.top = 1

	def parent(self, pos):
		return pos//2

	def left(self, pos):
		return pos * 2

	def right(self, pos):
		return (pos * 2) + 1

	def leaf(self, pos):
		return (pos >= self.size//2) and (pos <= self.size)

	def swap(self, pos1, pos2):
		self.mem[pos1], self.mem[pos2] = self.mem[pos2], self.mem[pos1]

	def push(self, element):
		if self.size >= self.maxsize:
			return

		self.size += 1
		self.mem[size] = element

		curr = self.size
		while self.mem[curr] > self.mem[parent(curr)]:
			self.swap(curr, parent(curr))
			curr = parent(curr)

	def pop(self):
		if self.size <= 0:
			return

		top = self.top
		self.mem[self.top] = self.mem[self.size]

		self.size -= 1
		self.heapify(self.top)

		return top

	def heapify(self, pos):
		curr = pos
		while (not self.leaf(curr)) and (self.mem[curr] < self.mem[self.left(curr)] or self.mem[curr] < self.mem[self.right(curr)]):
			if self.left(curr) < self.right(curr):
				self.swap(curr, left(curr))
				curr = left(curr)
			else:
				self.swap(curr, right(curr))
				curr = right(curr)

