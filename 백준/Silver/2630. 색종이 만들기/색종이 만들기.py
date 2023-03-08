N=int(input())
color=[[] for i in range(N)]
for i in range(N):
  color[i]=list(map(int, input().split()))


def cut(paper, N):
  global white, blue
  for i in range(N):
    for j in range(N):
      if paper[0][0]==paper[i][j]:
        continue
      else:
        paper1=[]
        for k1 in range(int(N/2)):
          paper1.append(paper[k1][:int(N/2)])
        paper2=[]
        for k2 in range(int(N/2)):
          paper2.append(paper[k2][int(N/2):])
        paper3=[]
        for k3 in range(int(N/2), int(N/2)*2):
          paper3.append(paper[k3][:int(N/2)])
        paper4=[]
        for k4 in range(int(N/2), int(N/2)*2):
          paper4.append(paper[k4][int(N/2):])
        return [cut(paper1, int(N/2)), cut(paper2, int(N/2)), cut(paper3, int(N/2)), cut(paper4, int(N/2))]
  if paper[0][0]==0:
    white+=1
  else:
    blue+=1

white, blue= 0, 0
cut(color, N)
print(white)
print(blue)