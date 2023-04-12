n=int(input())
stack=[0]
a=0
breaking=False
operator=[]
for _ in range(n):
    number=int(input())
    while True:
        if stack[-1]==number:
            stack.pop()
            operator.append("-")
            break
        else:
            a+=1
            stack.append(a)
            operator.append("+")
        if a>n:
            breaking=True
            break
    if breaking:
        break
if not breaking:
    for i in operator:
        print(i)
else:
    print("NO")