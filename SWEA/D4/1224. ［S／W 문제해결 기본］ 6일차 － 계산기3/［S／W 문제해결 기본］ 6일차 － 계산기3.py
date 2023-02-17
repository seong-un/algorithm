for test_case in range(10):
  length=int(input())
  string=list(input())
  stack=[]
  result=[]
  for s in string:
    if s=='(':
      stack.append(s)
    elif s.isnumeric():
      result.append(s)
    elif s=='*':
      while True:
        if stack[-1]=='*':
          result.append(stack.pop())
        else:
          stack.append(s)
          break
    elif s=='+':
      while True:
        if stack[-1]=='*':
          result.append(stack.pop())
        else:
          stack.append(s)
          break
    else:
      while True:
        if stack[-1] in ['*', '+']:
          result.append(stack.pop())
        else:
          stack.pop()
          break
  stack=[]
  for r in result:
    if r=='+':
      stack.append(stack.pop()+stack.pop())
    elif r=='*':
      stack.append(stack.pop()*stack.pop())
    else:
      stack.append(int(r))
  print(f'#{test_case+1} {stack.pop()}')