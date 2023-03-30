from collections import deque

def check(i, j):
    for k in queen:
        if k[1]==j:
            return False
        if k[0]-k[1]==i-j:
            return False
        if k[0]+k[1]==i+j:
            return False
    return True


def Queen(i, N):
    global cnt
    if i==N:
        cnt+=1
        return
    for j in range(N):
        if check(i, j):
            queen.append((i,j))
            Queen(i+1,N)
            queen.pop()

T=int(input())
for test_case in range(1, T+1):
        N=int(input())
        cnt=0
        queen=deque()
        Queen(0, N)
        print(f'#{test_case} {cnt}')