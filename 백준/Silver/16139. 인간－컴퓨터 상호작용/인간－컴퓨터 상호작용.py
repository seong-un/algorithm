S = input()
Q = int(input())
for q in range(Q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    result = 0
    for i in S[l:r+1]:
        if a==i:
            result += 1
    print(result)