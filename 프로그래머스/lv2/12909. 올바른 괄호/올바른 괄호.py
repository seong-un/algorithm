def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == "(":
            stack.append(True)
        else:
            try:
                stack.pop()
            except:
                answer = False
                break

    if stack:
        answer = False
        
    return answer