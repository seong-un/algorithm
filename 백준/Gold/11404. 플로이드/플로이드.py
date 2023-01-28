n=int(input())
m=int(input())
cost=[]
for i in range(m):
  cost.append(list(map(int, input().split())))
least=[[9999999]*n for i in range(n)]
for i in cost:
  least[i[0]-1][i[1]-1]=min(i[2], least[i[0]-1][i[1]-1])
for i in range(n):
  least[i][i]=0

for k in range(n):
  for j in range(n):
    for i in range(n):
      if least[i][j]>least[i][k]+least[k][j]:
        least[i][j]=least[i][k]+least[k][j]

for i in range(n):
  for j in range(n):
    if least[i][j]==9999999:
      least[i][j]=0

for i in least:
  print(*i)