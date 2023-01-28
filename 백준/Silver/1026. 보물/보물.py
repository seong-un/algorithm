N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

sum=0
A=sorted(A)
B=sorted(B, reverse=True)
for i in range(N):
  sum+=A[i]*B[i]

print(sum)