N=int(input())
A=list(map(int, input().split()))
dp=[1]*N
for j in range(1, N):
    for i in range(j):
        if A[j]>A[i]:
            dp[j]=max(dp[j], dp[i]+1)
print(max(dp))