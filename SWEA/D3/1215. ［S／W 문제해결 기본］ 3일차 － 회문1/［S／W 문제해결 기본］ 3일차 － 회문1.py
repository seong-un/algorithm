for test_case in range(1, 11):
    length=int(input())
    keyboard=[0]*8
    for i in range(8):
        keyboard[i]=input()
    cnt=0
    for s in keyboard:
        for i in range(8-length+1):
            if s[i:i+length]==''.join(list(reversed(s[i:i+length]))):
                cnt+=1
    for s in list(zip(*keyboard)):
        for i in range(8-length+1):
            if list(s)[i:i+length]==list(reversed(list(s)[i:i+length])):
                cnt+=1
    print(f'#{test_case} {cnt}')