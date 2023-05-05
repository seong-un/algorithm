n, m=map(int, input().split())
A=list(map(int, input().split()))
A=sorted(A)
for _ in range(m):
    Q, *rng=map(int, input().split())
    for_con=False
    if Q==1:
        for idx, i in enumerate(A):
            if i>=rng[0]:
                print(n-idx)
                for_con=True
                break
        if not for_con:
            print(0)
    elif Q==2:
        for idx, i in enumerate(A):
            if i>rng[0]:
                print(n-idx)
                for_con=True
                break
        if not for_con:
            print(0)
    else:
        for idx, i in enumerate(A):
            if i>=rng[0]:
                a=idx
                for_con=True
                break
        if not for_con:
            print(0)
            continue
        for_con=False
        for jdx, j in enumerate(A[a:]):
            if j>rng[1]:
                print(jdx)
                for_con=True
                break
        if not for_con:
            print(n-idx)