for test_case in range(10):
    N=int(input())
    string=list(input())
    stack=[]
    for i in string:
        if i.isnumeric():
            if stack:
                a=stack.pop()
                stack.append(i)
                stack.append(a)
            else:
                stack.append(i)
        else:
            stack.append(i)

    calculator=[]
    for i in stack:
        if i.isnumeric():
            calculator.append(i)
        else:
            calculator.append(int(calculator.pop())+int(calculator.pop()))

    print(f'#{test_case+1} {int(calculator.pop())}')