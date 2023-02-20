T=int(input())
for test_case in range(1, T+1):
    string=input()
    s=1
    while True:
        while True:
            if string[:s]!=string[s:2*s]:
                s+=1
            else:
                word=string[:s]
                break
        if (word*(int(30//len(word))+1))[:30]==string:
            print(f'#{test_case} {len(word)}')
            break
        else:
            s+=1