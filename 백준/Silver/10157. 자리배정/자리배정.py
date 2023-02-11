C, R=map(int, input().split())
K=int(input())
idx=0
seat=0
while idx+2*(C+R)-4<K and C>0 and R>0:
  idx+=2*(C+R)-4
  C-=2
  R-=2
  seat+=1
if C>0 and R>0:
  if K-idx<=R:
    print(seat+1, seat+K-idx)
  elif K-idx<=R+C-1:
    print(seat+1+K-idx-R, R+seat)
  elif K-idx<=2*R+C-2:
    print(C+seat, 2*R-K+idx+C-1+seat)
  else:
    print(2*(R+C)-K+idx-2+seat, 1+seat)
else:
  print(0)