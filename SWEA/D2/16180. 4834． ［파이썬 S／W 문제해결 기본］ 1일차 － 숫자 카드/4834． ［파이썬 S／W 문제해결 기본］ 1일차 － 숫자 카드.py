T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ai=list(map(int, input()))
    L=[0]*10

		# 해당 인덱스에 있는 숫자를 1 증가시킨다. 그러한 숫자 카운트를 담은 리스트 L
    for i in ai:
        L[i]+=1
    mx=L[0]
    cnt=-1 # 카드가 가장 많은 숫자인 mxcnt를 뽑기 위한 cnt는 거들 뿐.
    mxcnt=0 # 카드가 가장 많은 숫자 mxcnt
    for i in L:
        cnt+=1 # for문 돌때마다 1씩 증가
        if i>=mx: # 같은 숫자일 때 가장 큰 값을 뽑기 위해 같을 때도 포함시킴.
            mx=i
            mxcnt=cnt
    print(f'#{test_case} {mxcnt} {mx}')