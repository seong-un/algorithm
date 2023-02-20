T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    farm=[0]*N
    for f in range(N):
        farm[f]=input()
    crop=0
    for i in range(N):
        crop+=sum(map(int, farm[i][abs(N-N//2-i-1):N//2+abs(N//2-abs(N-N//2-i-1))+1]))
    print(f'#{test_case} {crop}')