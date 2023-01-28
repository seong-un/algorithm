import sys
input = sys.stdin.readline

N, L=map(int, input().split())
water=sorted(map(int, input().split()))
tape=0

def isBiggerThanEnd(x):
  return x>end
for i in range(len(water)):
  if len(water)<=1 or L==1:
    tape+=len(water)
    break
  if water[1]-water[0]<=L-1:
    tape+=1
    end=water[0]+L-1
    water=list(filter(isBiggerThanEnd, water))
  else:
    tape+=1
    del water[0]
              
print(tape)