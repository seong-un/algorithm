T = int(input())
for t in range(T):
    N = int(input())
    alcohol = []
    for n in range(N):
        S, L = input().split()
        L = int(L)
        alcohol.append([S, L])
    print(max(alcohol, key = lambda x:x[1])[0])