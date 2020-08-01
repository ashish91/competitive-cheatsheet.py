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