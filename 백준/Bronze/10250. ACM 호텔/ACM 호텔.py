T=int(input())
for _ in range(T):
    H, W, N=map(int, input().split())
    if N%H!=0:
        floor=N%H
        one=N//H+1
    else:
        floor=H
        one=N//H
    print(floor*100+one)