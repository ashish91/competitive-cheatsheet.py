import math

def is_prime(a):
  if a <= 1:
    return False

  for i in range(2, math.sqrt(a)+1):
    if a%i == 0:
      return False

  return True
