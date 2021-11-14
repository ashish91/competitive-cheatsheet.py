# Optimized
# Here we're looping no of SET bits times
def count(N):
  bits = 0
  while N > 0:
    N = N&(N-1)
    bits += 1

  return bits

T: O(log(N))

# Here we're looping no of bits times
def count(N):
  bits = 0
  for i in range(31):
    if N&(1<<i) == 1:
      bits += 1

  return bits
