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