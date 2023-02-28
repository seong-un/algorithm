T=int(input())
for test_case in range(1, T+1):
    word=[0]*5
    L=0
    for i in range(5):
        word[i]=list(input())
        if L<len(word[i]):
            L=len(word[i])
    for i in range(5):
        if len(word[i])!=L:
            word[i].extend(['?']*(L-len(word[i])))
    result=''
    for i in list(zip(*word)):
        for j in i:
            result+=j
    print(f"#{test_case} {result.replace('?', '')}")