T=int(input())
for test_case in range(1, T+1):
    bit=input()
    correct=0
    current='0'
    for b in bit:
        if current=='0':
            if b=='1':
                correct+=1
                current='1'
        else:
            if b=='0':
                correct+=1
                current='0'
    print(f'#{test_case} {correct}')