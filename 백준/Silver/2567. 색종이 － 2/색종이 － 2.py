N=int(input())
paper=[[0]*101 for i in range(101)]
for i in range(N):
    x, y=map(int, input().split())
    for j in range(10):
        paper[x+j][y:y+10]=[1]*10
cnt=0
for i in range(101):
    for j in range(100):
        if paper[i][j]+paper[i][j+1]==1:
            cnt+=1
        if paper[j][i]+paper[j+1][i]==1:
            cnt+=1
print(cnt)