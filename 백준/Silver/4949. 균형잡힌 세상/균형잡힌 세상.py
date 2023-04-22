while True:
    string = input()
    if string == '.':
        break
    parenthesis = []
    for i in string:
        if i in ('(', '['):
            parenthesis.append(i)
        elif i == ')':
            try:
                if parenthesis.pop() == '(':
                    continue
                else:
                    print("no")
                    break
            except:
                print("no")
                break
        elif i == ']':
            try:
                if parenthesis.pop() == '[':
                    continue
                else:
                    print("no")
                    break
            except:
                print("no")
                break
        elif i == '.':
            if parenthesis:
                print("no")
            else:
                print("yes")
