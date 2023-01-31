# Multiply by 2
N = N << 1
# Divide by 2
N = N >> 1
# N is odd
N&1 == 1
# N is even
N&1 == 0
# N's ith bit is set
N&(1<<i) == 1
# Power of 2 check
N & (N-1) == 0

# XOR
a^a = 0
a^0 = a
