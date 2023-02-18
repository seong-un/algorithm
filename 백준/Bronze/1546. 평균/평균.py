N=int(input())
score=list(map(int, input().split()))
sm=0
for s in score:
  sm+=s/max(score)*100
print(sm/len(score))