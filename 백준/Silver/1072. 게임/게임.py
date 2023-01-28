import math
X, Y=map(int, input().split())

sum=0
def binary(y,x):
  global sum
  i=0
  while True:
    if (y*100)//x>=99:
      return -1
      break
    if (y*100)//x!=((y+2**i)*100)//(x+2**i):
      if i!=0:
        sum+=2**(i-1)
        return binary(y+2**(i-1), x+2**(i-1))
      if i==0:
        return sum+1
    i+=1

print(binary(Y,X))