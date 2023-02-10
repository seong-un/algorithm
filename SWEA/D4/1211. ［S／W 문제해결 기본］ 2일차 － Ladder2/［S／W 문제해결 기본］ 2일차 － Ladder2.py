for _ in range(10):
    test_case=int(input())
    ladder=[0]*100
    for i in range(100):
        ladder[i]=list(map(int, input().split()))
    start=[]
    for idx, i in enumerate(ladder[0]):
        if i==1:
            start.append(idx)
    cnt=[0]*len(start)
    for idx, i in enumerate(start):
        vertex=i
        floor=0
        while floor<=99:
            if vertex==0:
                if ladder[floor][vertex+1]==1:
                    cnt[idx]+=start[start.index(vertex)+1]-vertex
                    vertex=start[start.index(vertex)+1]
                    floor+=1
                else:
                    floor+=1
            elif vertex==99:
                if ladder[floor][vertex-1]==1:
                    cnt[idx]+=vertex-start[start.index(vertex)-1]
                    vertex=start[start.index(vertex)-1]
                    floor+=1
                else:
                    floor+=1
            else:
                if ladder[floor][vertex+1]==1:
                    cnt[idx]+=start[start.index(vertex)+1]-vertex
                    vertex=start[start.index(vertex)+1]
                    floor+=1
                else:
                    if ladder[floor][vertex - 1] == 1:
                        cnt[idx] += vertex - start[start.index(vertex) - 1]
                        vertex = start[start.index(vertex) - 1]
                        floor+=1
                    else:
                        floor += 1
    print(f'#{test_case} {start[cnt.index(min(cnt))]}')