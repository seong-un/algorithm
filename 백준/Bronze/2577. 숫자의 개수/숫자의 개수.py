A=int(input())
B=int(input())
C=int(input())
AxBxC=[0]*10
for i in str(A*B*C):
    AxBxC[int(i)]+=1
for i in AxBxC:
    print(i)