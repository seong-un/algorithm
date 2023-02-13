for t in range(1, 11):
    _, num=input().split()
    num=list(num)
    cnt=1
    while cnt!=0:
        number = len(num)
        cnt=0
        for w in range(number-1):
            if num[w]==num[w+1]:
                num.pop(w+1)
                num.pop(w)
                cnt+=1
                break
    print(f'#{t} ', *num, sep='')