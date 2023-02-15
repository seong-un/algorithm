T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    room=[0]*N
    for i in range(N):
        room[i]=list(map(int, input().strip().split()))
    flow=[0]*200
    for i in room:
        if i[0]<i[1]:
            for j in range((i[0]-1)//2, (i[1]-1)//2+1):
                flow[j]+=1
        else:
            for j in range((i[1]-1)//2, (i[0]-1)//2+1):
                flow[j]+=1
    print(f'#{test_case} {max(flow)}')