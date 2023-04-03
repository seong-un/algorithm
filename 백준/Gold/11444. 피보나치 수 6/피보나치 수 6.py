import sys
input=sys.stdin.readline

n=int(input())
def fibonacci(n):
    if dp.get(n)!=None:
        return dp[n]
    if n<=0:
        return 0
    if n in [1,2]:
        return 1
    if n%2==1:
        dp[(n+1)//2]=fibonacci((n+1)//2)%1000000007
        dp[(n+1)//2-1]=fibonacci((n+1)//2-1)%1000000007
        return dp[(n+1)//2]**2+dp[(n+1)//2-1]**2
    else:
        dp[n//2-1]=fibonacci(n//2-1)%1000000007
        dp[n//2]=fibonacci(n//2)%1000000007
        return (2*dp[n//2-1]+dp[n//2])*dp[n//2]

dp=dict()
print(fibonacci(n)%1000000007)