
N, L, R, X = map(int, input().split()) # 문제 수 N, R >= 난이도 합 >= L, 최대-최소 >= X 

A = list(map(int,input().split())) # 난이도
check = [0] * N
cnt = 0

# 부분 수열 구해서 조건 걸기

def subset(idx):
    global cnt
    if idx == N:
        arr = []
        for i in range(N):
            if check[i] == 1:
                arr.append(A[i])
        # print(arr)
        if L <= sum(arr) <= R and max(arr)-min(arr) >= X:
            cnt += 1
        return
    
    check[idx] = 0
    subset(idx+1)
    check[idx] = 1
    subset(idx+1)

subset(0)

print(cnt) # 문제 고르는 방법의 수