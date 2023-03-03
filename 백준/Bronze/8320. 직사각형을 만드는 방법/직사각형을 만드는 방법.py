N=int(input())
cnt=0
for i in range(1, N+1):
    for j in range(1, int(i**(1/2))+1):
        if i%j==0:
            cnt+=1
print(cnt)