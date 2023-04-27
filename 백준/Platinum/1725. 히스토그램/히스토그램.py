while True:
    N = int(input())
    lst = [int(input()) for _ in range(N)]
        
    stack = []
    max_rlt = 0
    
    stack = []
    max_v = 0
    for i in range(N):
        idx = i
        while stack and stack[-1][1] > lst[i]: 
            idx, height = stack.pop()
            rst = (i - idx) * height
            max_v = max(max_v, rst)
        stack.append((idx, lst[i]))

    while stack:
        idx, height = stack.pop()
        rst = (N - idx) * height
        max_v = max(max_v, rst)
    print(max_v)

    break
