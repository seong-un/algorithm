from collections import deque

def solution(queue1, queue2):
    answer = 0
    s1, s2 = sum(queue1), sum(queue2)
    l1, l2 = len(queue1), len(queue2)
    l12 = l1 + l2
    i1, i2 = 0, l1
    sum_queue = queue1 + queue2
    while True:
        if s1 > s2:
            qi1 = sum_queue[i1]
            s1 -= qi1
            s2 += qi1
            i1 += 1
            if i1 == l12:
                i1 = 0
        elif s1 < s2:
            qi2 = sum_queue[i2]
            s2 -= qi2
            s1 += qi2
            i2 += 1
            if i2 == l12:
                i2 = 0
        else:
            break
        answer += 1
        if i1 == l12 or i2 == l1 - 1:
            answer = -1
            break
    return answer