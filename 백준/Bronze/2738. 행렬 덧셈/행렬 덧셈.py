N, M=map(int, input().split())
A=[]
for i in range(N):
    A.append(list(map(int, input().split())))
B=[]
for i in range(N):
    B.append(list(map(int, input().split())))
C=[[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        C[i][j]=A[i][j]+B[i][j]
for i in C:
    print(*i)