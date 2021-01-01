# Initialise 1D array
arr = [ 1 for i in range(3) ]
arr = [1]*3 # [1, 1, 1]

# Initialise 2D array
matrix = [[0 for c in range(cols)] for r in range(rows)]
matrix = [[0]*cols]*rows

# Loop By Element
for element in arr:
  print(element)
# Loop By Index
for index in range(arr):
  print(arr[index])
# Loop By Index and Element
for index, element in enumerate(arr):
  print('Element: ' + element)
  print('Index: ' + index)
# Loop in Reverse
for element in reversed(arr):
  print('Element: ' + element)
for index in range(len(arr)-1, -1, -1):
  print('Element: ' + element)

# Sorting an array
arr.sort()
arr.sort(reverse=True)

# Reverse
arr = arr[::-1]
reversed(arr)

# Subarray
arr = [1,2,3,4]
a[0:1]
[1]
a[2:4]
[3,4]

# Add element
arr.append(24)
# Add element at ith position
arr.insert(i,24)

# Remove element from back
arr.pop()
# Remove element at ith position
arr.pop(i)
