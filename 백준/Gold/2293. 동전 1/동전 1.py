n, k=map(int, input().split())
coin=[0]*n
for i in range(n):
    coin[i]=int(input())
dp=[0]*10001
a=coin[0]
dp[0]=1
for i in coin:
    for j in range(i, k+1):
        dp[j]+=dp[j-i]
print(dp[k])