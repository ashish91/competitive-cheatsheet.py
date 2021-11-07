A%M = [0,M-1]

(A+B)%M = (A%M + B%M)%M
Additional mod is to make it in range [0,m-1]

(A-B)%M = (A%M-B%M+M)%M

(A%M-B%M) is in range [-M+1,M-1]
To make it [0,M-1] we add M

(A*B)%M = (A%M * B%M)%M
Same as addition

(A^B)%M = (A * A * A * .... * A)%M B times
        = (A%M * A%M * A%M * .... * A%M)

product = 1
A = A%M
for i in range(B):
  product = (product * A)%M


Fermat's Theorem
(A^(P-1))%P = 1 where P is a prime number

(A^B)%P = (A^(P-1) * A^(P-1) * A^(P-1) * ... * A^(b%(P-1)))%P
        = (1 * 1 * 1 * ... * A^(b%(P-1)))%P Using Fermat's Theorem
        = (A^(b%(P-1)))%P
