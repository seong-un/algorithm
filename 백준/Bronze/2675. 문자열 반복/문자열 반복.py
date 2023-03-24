T=int(input())
for t in range(T):
    R, S=input().split()
    R=int(R)
    S=list(S)
    string=''
    for i in S:
        string+=i*R
    print(string)