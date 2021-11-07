Properties of GCD

- gcd(a,b) = gcd(b,a)
- gcd(a,0) = gcd(a,0)
- gcd(a,1) = 1
- gcd(a,b-a) = gcd(a,b) for b >= a
- gcd(a,b) = gcd(a,b%a)

def gcd(a,b):
  if (b == 0) return a
  return gcd(b,a%b)

Time complexity of gcd(a,b) = log(max(a,b))

- gcd(a,gcd(b,c)) = gcd(gcd(a,b),c)
