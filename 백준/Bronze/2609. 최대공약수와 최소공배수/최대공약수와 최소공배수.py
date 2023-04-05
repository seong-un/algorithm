N, M=map(int, input().split())
total=N*M
a=2
common=1
if N==1 or M==1:
    pass
else:
    while a<=min([N,M]):
        if N%a!=0 or M%a!=0:
            a+=1
            continue
        N=N//a
        M=M//a
        common*=a
print(common)
print(total//common)