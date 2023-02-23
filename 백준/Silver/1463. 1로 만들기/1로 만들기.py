N=int(input())
one=[0, 1, 1]
for i in range(4, N+1):
    if i%6==0:
        one.append(1+min(one[int(round(i/3))-1], one[int(round(i/2))-1], one[i-2]))
    elif i%3==0:
        one.append(1+min(one[int(round(i/3))-1], one[i-2]))
    elif i%2==0:
        one.append(1+min(one[int(round(i/2))-1], one[i-2]))
    else:
        one.append(1+one[i-2])
print(one[N-1])