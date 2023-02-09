def check(bingo):
    cnt=0
    for i in bingo:
        if i==[0,0,0,0,0]:
            cnt+=1
    for i in list(zip(*bingo)):
        if i==(0,0,0,0,0):
            cnt+=1
    if [bingo[i][i] for i in range(5)]==[0,0,0,0,0]:
        cnt+=1
    if [bingo[i][4-i] for i in range(5)]==[0,0,0,0,0]:
        cnt+=1
    if cnt>=3:
        return 1
    else:
        return 0

try:
    bingo=[0]*5
    for i in range(5):
        bingo[i]=list(map(int, input().split()))

    idx=0
    for_break=0
    for i in range(5):
        A, B, C, D, E=map(int, input().split())
        for b in bingo:
            if A in b:
                idx+=1
                bingo[bingo.index(b)][b.index(A)]=0
                if check(bingo):
                    print(idx)
                    for_break=1
        if for_break == 1:
            break
        for b in bingo:
            if B in b:
                idx += 1
                bingo[bingo.index(b)][b.index(B)] = 0
                if check(bingo):
                    print(idx)
                    for_break = 1
        if for_break == 1:
            break
        for b in bingo:
            if C in b:
                idx += 1
                bingo[bingo.index(b)][b.index(C)] = 0
                if check(bingo):
                    print(idx)
                    for_break = 1
        if for_break == 1:
            break
        for b in bingo:
            if D in b:
                idx += 1
                bingo[bingo.index(b)][b.index(D)] = 0
                if check(bingo):
                    print(idx)
                    for_break = 1
        if for_break == 1:
            break
        for b in bingo:
            if E in b:
                idx += 1
                bingo[bingo.index(b)][b.index(E)] = 0
                if check(bingo):
                    print(idx)
                    for_break = 1
        if for_break == 1:
            break
except:pass