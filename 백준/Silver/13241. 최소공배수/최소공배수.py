A, B = map(int, input().split())
l = A if A < B else B
while True:
    if A % l == 0:
        if B % l == 0:
            break
    l -= 1
print(A*B//l)