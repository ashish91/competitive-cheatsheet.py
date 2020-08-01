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
