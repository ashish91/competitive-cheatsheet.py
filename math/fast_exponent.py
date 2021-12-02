def fast_exponent(num,exp):
  if exp == 0:
    return 1
  if exp%2 == 0:
    return fast_exponent(num*num, exp//2)
  else:
    return num*fast_exponent(num, exp-1)
