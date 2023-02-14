T=int(input())
for test_case in range(1, T+1):
    iron=input()
    iron=iron.replace('()', '/')
    cnt=0
    result=0
    for i in iron:
        if i=='(':
            cnt+=1
        elif i=='/':
            result+=cnt
        else:
            cnt-=1
            result+=1
    print(f'#{test_case} {result}')