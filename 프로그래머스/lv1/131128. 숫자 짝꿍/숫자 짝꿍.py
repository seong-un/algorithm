def solution(X, Y):
    answer = ''
    list_inter = []
    
    for i in range(9, -1, -1):
        s = str(i)
        answer += s * min([X.count(s), Y.count(s)])
    
    if not answer:
        return "-1"
    elif len(answer) == answer.count('0'):
        return "0"
    else:
        return answer