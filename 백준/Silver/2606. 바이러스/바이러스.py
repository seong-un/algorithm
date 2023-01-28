computer=int(input())
edge=int(input())
pair=[]
for i in range(edge):
  pair.append(list(map(int, input().split())))

first=[1]
def bfs(x):
  global first
  second=[]
  for i in range(edge):
    for j in range(2):
      if pair[i][j]==x:
        if j==0:
          second.append(pair[i][1])
        else:
          second.append(pair[i][0])
  sum=0
  for i in range(len(second)):
    sum+=(second[i] in first)
  if len(second)==sum:
    return first
  else:
    first+=second
    first=list(set(first))
  for i in range(len(second)):
    bfs(second[i])

bfs(1)
print(len(first)-1)