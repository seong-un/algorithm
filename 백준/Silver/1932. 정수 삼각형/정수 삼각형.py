n=int(input())
triangle=[0]*n
triangle[0]=int(input())
for i in range(1, n):
    result=triangle[:]
    t=list(map(int, input().split()))
    for j in range(i+1):
        if j not in [0,i]:
            triangle[j]=max([result[j]+t[j], result[j-1]+t[j]])
        elif j==0:
            triangle[j]=result[j]+t[j]
        else:
            triangle[j]=result[j-1]+t[j]
print(max(triangle))