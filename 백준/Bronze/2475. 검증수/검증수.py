number=list(map(int, input().split()))
sm=0
for n in number:
  sm+=n**2
print(sm%10)