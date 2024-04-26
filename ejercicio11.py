def ackerman(m, n):
  if m==0:
    return n+1
  if m>0 and n==0:
    return ackerman(m-1, 1)
  # if m>0 and n>0:
  return ackerman(m-1, ackerman(m,n-1))

print(ackerman(2,3))
