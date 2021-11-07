def fast_exponent(num,exp):

  if exp == 0:
    return 1

  if num%2 == 0:
    return fast_exponent(num*num, exp/2)
  else:
    return num*fast_exponent(num*num, (exp-1)/2)
