N=int(input())
jerge=[[] for i in range(N)]
for i in range(N):
  age, name=input().split()
  age=int(age)
  jerge[i]=[age, name]
for i in sorted(jerge, key=lambda x:x[0]):
  print(*i)