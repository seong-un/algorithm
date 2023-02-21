from collections import deque

for _ in range(10):
    T=int(input())
    password=deque(map(int, input().split()))
    mn=min(password)
    for i in range(8):
        password[i]-=15*int((mn-5)/15)
    a=1
    while True:
        p=password.popleft()-a
        if p<=0:
            p=0
            password.append(p)
            break
        password.append(p)
        if a!=5:
            a+=1
        else:
            a=1
    print(f'#{T}', *password)