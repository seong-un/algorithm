T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    a,b,c,d,e=0,0,0,0,0
    while True:
        if N%2==0:
            N=N/2
            a+=1
        else:
            break
    while True:
        if N%3==0:
            N=N/3
            b+=1
        else:
            break
    while True:
        if N%5==0:
            N=N/5
            c+=1
        else:
            break
    while True:
        if N%7==0:
            N=N/7
            d+=1
        else:
            break
    while True:
        if N%11==0:
            N=N/11
            e+=1
        else:
            break
    print(f'#{test_case} {a} {b} {c} {d} {e}')