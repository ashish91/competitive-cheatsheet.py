import math

def factors(a):
  if a <= 1:
    return [a]

  facts = []
  for i in range(2, math.sqrt(a)+1):
    if a%i == 0:
      facts.append(i)
      if a//i != i:
        facts.append(a//i)

  return facts
