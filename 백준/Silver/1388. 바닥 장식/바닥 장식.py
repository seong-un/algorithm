N, M=map(int, input().split())

floor=[]
for i in range(N):
  floor.append(input())

tile_list=[]
for i in range(N):
  tile=0
  if floor[i][0]=="-":
    tile+=1
  for j in range(M-1):
    if floor[i][j]!=floor[i][j+1]:
      tile+=1
  tile_list.append((tile+1)//2)

for j in range(M):
  tile=0
  if floor[0][j]=="|":
    tile+=1
  for i in range(N-1):
    if floor[i][j]!=floor[i+1][j]:
      tile+=1
  tile_list.append((tile+1)//2)

print(sum(tile_list))