import heapq

T=int(input())
for test_case in range(1, T+1):
    N, M, K=map(int, input().split())
    depart=list(map(int, input().split()))
    heapq.heapify(depart)
    for_break=False
    while depart:
        for j in range(M):
            for i in range(len(depart)):
                depart[i]-=1
            for i in depart:
                if i<0:
                    print(f'#{test_case} Impossible')
                    for_break=True
                    break
            if for_break:
                break
        for i in range(min(K, len(depart))):
            heapq.heappop(depart)
        if for_break:
            break
    if not for_break:
        print(f'#{test_case} Possible')