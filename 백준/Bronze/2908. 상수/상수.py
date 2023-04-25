A, B=input().split()
A=int(''.join(list(reversed(A))))
B=int(''.join(reversed(B)))
if A>B:
    print(A)
else:
    print(B)