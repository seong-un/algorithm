notation = list(input())
result = ''
stack = []
for idx, i in enumerate(notation):
  if 65 <= ord(i) <= 90:
    result+=i
  elif i=='(':
    stack.append(i)
  elif i in ['+', '-']:
    while stack and stack[-1]!='(':
      result+=stack.pop()
    stack.append(i)
  elif i in ['*', '/']:
    if not stack:
      stack.append(i)
    else:
      if stack[-1]=='(':
        stack.append(i)
      elif stack[-1] in ['+', '-']:
        stack.append(i)
      else:
        result+=stack.pop()
        stack.append(i)
  else:
    while stack[-1]!='(':
      result+=stack.pop()
    stack.pop()
while stack:
  result+=stack.pop()
print(result)