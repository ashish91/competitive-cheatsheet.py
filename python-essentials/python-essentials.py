## Reading input

## Strings

# ASCII
ascii = ord('a') # 97
# Finding Length
length = len(string)
# Concat
string1 = 'practice'
string2 = 'makes'
string3 = 'perfect'
string = string1 + string2 + string3
# Split
string = 'Practice, makes, perfect'
string = string.split(',')
# Looping
for char in string:
	print('Character: ' + char)

for index, char in enumerate(string):
	print('Character: ' + char)
	print('Character from index: ' + string[index])
# Substring
string[s:e] # Starting from s and ending at e
string[s:] # Starting from s
string[:e] # Starting from e
# Replacing
string = 'test test test test'
string.replace('test', 'testing', 3)
print(string) # 'testing testing testing test'

## Arrays

# Finding length
length = len(arr)
# Looping
for element in arr:
	print(element)
for index in range(arr):
	print(arr[index])
for index, element in enumerate(arr):
	print('Element: ' + element)
	print('Index: ' + index)
# Initialise 1D array
arr = [1]*3 # [1, 1, 1]
arr = [ 1 for i in range(3) ]
# Initialise 2D array
matrix = [[0 for i in range(cols)] for j in range(rows)]
matrix = [[0]*cols]*rows

## Dictionary


## Stack

# Initialise
stack = [1, 2, 3]
# Push
stack.append(1)
# Pop
stack.pop()
# Top
stack[-1]
# Length
length = len(stack)
# Print
print(stack)

## Queue

# Initialise
queue = [3, 2, 1]
# Enqueue
queue.append(1)
# Dequeue
queue.pop(0)
# Front
queue[0]
# Length
length = len(stack)
# Print
print(queue)

## Deque (Double Ended Queue)

## Heaps (Binary heap)
import heapq

# Initialise
heap = [1, 2, 3]
heapq.heapify(heap)       # min heap
heapq._heapify_max(heap)  # max heap
# Add
heapq.heappush(heap, 4)  													 # min heap
heapq.heappush(heap, 4); heapq._heapify_max(heap)  # max heap
# Remove
heapq.heappop(heap)      # min heap
heapq._heappop_max(heap) # max heap
# Root
heap[0]
# Length
length = len(stack)
# Print
print(list(heap))

