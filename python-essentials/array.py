# Finding length
length = len(arr)

# Looping
# By Element
for element in arr:
	print(element)
# By Index
for index in range(arr):
	print(arr[index])
# By Index and Element
for index, element in enumerate(arr):
	print('Element: ' + element)
	print('Index: ' + index)
# Reverse
for element in reversed(arr):
	print('Element: ' + element)
for index in range(len(arr)-1, -1, -1):
	print('Element: ' + element)

# Initialise 1D array
arr = [1]*3 # [1, 1, 1]
arr = [ 1 for i in range(3) ]

# Initialise 2D array
matrix = [[0 for i in range(cols)] for j in range(rows)]
matrix = [[0]*cols]*rows

# Sorting an array
arr.sort()
arr.sort(reverse=True)