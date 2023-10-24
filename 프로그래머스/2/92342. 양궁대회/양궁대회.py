from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    max_score = 0
    for scores_lion in list(combinations_with_replacement([i for i in range(11)], n)):
        apeach = 0
        lion = 0
        list_lion = [0 for i in range(11)]
        for score in scores_lion:
            list_lion[score] += 1
        for i in range(11):
            if info[i] == 0 and list_lion[i] == 0:
                continue
            if info[i] >= list_lion[i]:
                apeach += 10 - i
            else:
                lion += 10 - i
        if lion <= apeach:
            continue
        if max_score < lion - apeach:
            max_score = lion - apeach
            answer = list_lion
        elif max_score == lion - apeach:
            for i in range(10, -1, -1):
                if answer[i] > list_lion[i]:
                    break
                elif answer[i] < list_lion[i]:
                    answer = list_lion
                    break

    if not answer:
        answer = [-1]
    return answer