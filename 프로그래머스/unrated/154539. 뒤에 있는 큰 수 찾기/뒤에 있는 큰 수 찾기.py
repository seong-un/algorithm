def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and stack[-1][0] < numbers[i]:
            popen = stack.pop()
            answer[popen[1]] = numbers[i]
        stack.append([numbers[i], i])
            
    return answer