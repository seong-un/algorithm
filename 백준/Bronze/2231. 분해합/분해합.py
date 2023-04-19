N = int(input())
constructor = 1
while constructor<N:
    if N == constructor + sum(map(int, list(str(constructor)))):
        print(constructor)
        break
    constructor += 1
if constructor == N:
    print(0)