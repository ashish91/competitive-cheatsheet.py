def prefix_sum(arr):
  n = len(arr)
  prefix = [0] * n
  for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]

  return prefix
