import math
def sieve_of_eratosthenes(N):
  is_prime = [True]*(N+1)
  is_prime[0] = is_prime[1] = 0

  primes = []
  for i in range(2, math.sqrt(N)+1):
    if is_prime[i]:
      primes.append(i)
      for j in range(i*i,N+1,i):
        is_prime[j] = False

  return primes

# TC: O(Nlog(log(N)))
# SC: O(N)
