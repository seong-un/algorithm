w, h=map(int, input().split())
p, q=map(int, input().split())
t=int(input())

if (p+t)//w%2==0:
  horizon=(p+t)%w
else:
  horizon=w-(p+t)%w
if (q+t)//h%2==0:
  vertex=(q+t)%h
else:
  vertex=h-(q+t)%h
print(horizon, vertex)