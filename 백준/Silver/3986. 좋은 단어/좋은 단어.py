N = int(input())
result = 0
for n in range(N):
    string = input()
    stack = [0]
    for s in string:
        if s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    if stack == [0]:
        result += 1
print(result)