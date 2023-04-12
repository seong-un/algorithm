T=int(input())
for t in range(T):
    quiz=input()
    stack=0
    score=0
    for i in quiz:
        if i=='O':
            stack+=1
        else:
            stack=0
        score+=stack
    print(score)