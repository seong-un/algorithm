def turn_Desert(x,y,cnt, turn_cnt):
    global desert, result
    turn_cnt+=1
    if x>N-1 or y>N-1 or cafe[x][y] in desert:
        return
    desert.append(cafe[x][y])
    turn_Desert(x+1, y+1, cnt, turn_cnt)
    desert_copy=desert[:]
    if x+cnt>N-1 or y-cnt<0:
        desert.pop()
        return
    for i in range(1, cnt+1):
        desert.append(cafe[x+i][y-i])
    a=x+cnt
    b=y-cnt
    for i in range(1, turn_cnt):
        desert.append(cafe[a-i][b-i])
    if len(desert)==len(set(desert)):
        result=max(result, len(desert))
    desert=desert_copy[:]
    desert.pop()

def Desert(x, y, cnt, turn_cnt):
    cnt+=1
    if x<0 or y>N-1 or cafe[x][y] in desert:
        return
    desert.append(cafe[x][y])
    Desert(x-1, y+1, cnt, turn_cnt)
    if len(desert)==1:
        return
    turn_Desert(x+1, y+1, cnt, turn_cnt)
    desert.pop()

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    cafe=[list(map(int, input().split())) for i in range(N)]
    result=0
    for v in range(1, N-1):
        for w in range(N-2):
            desert=[]
            turn_cnt=0
            cnt=-1
            Desert(v, w, cnt, turn_cnt)
    if result==0:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {result}')