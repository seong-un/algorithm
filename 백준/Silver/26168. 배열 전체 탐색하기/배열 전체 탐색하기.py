import sys
input=sys.stdin.readline

n, m=map(int, input().split())
A=list(map(int, input().split()))
A=sorted(A)
for _ in range(m):
    Q, *rng=map(int, input().split())
    for_con=False
    if Q==1:
        start=0
        end=n
        try:
            while start<=end:
                mid=(start+end)//2
                if A[mid]>=rng[0]:
                    if A[mid-1]<rng[0]:
                        print(n-mid)
                        for_con=True
                        break
                    else:
                        end=mid-1
                else:
                    start=mid+1
            if not for_con:
                print(n)
        except:
            print(0)
    elif Q==2:
        start=0
        end=n
        try:
            while start<=end:
                mid=(start+end)//2
                if A[mid]>rng[0]:
                    if A[mid-1]<=rng[0]:
                        print(n-mid)
                        for_con=True
                        break
                    else:
                        end=mid-1
                else:
                    start=mid+1
            if not for_con:
                print(n)
        except:
            print(0)
    else:
        start=0
        end=n
        a=n
        try:
            while start<=end:
                mid=(start+end)//2
                if A[mid]>=rng[0]:
                    if A[mid-1]<rng[0]:
                        a=mid
                        for_con=True
                        break
                    else:
                        end=mid-1
                else:
                    start=mid+1
            if not for_con:
                a=0
        except:
            print(0)
            continue
        start=0
        end=n
        b=n
        try:
            while start<=end:
                mid=(start+end)//2
                if A[mid]<=rng[1]:
                    if A[mid+1]>rng[1]:
                        b=mid
                        break
                    else:
                        start=mid+1
                else:
                    end=mid-1
        except:
            print(n-a)
            continue
        print(b-a+1)