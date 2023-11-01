dx = [1, -1, 0, 0, 1, -1, 1, -1, 2, -2, 0, 0]
dy = [0, 0, 1, -1, 1, 1, -1, -1, 0, 0, 2, -2]

def solution(places):
    answer = []
    for place in places:
        for idx, line in enumerate(place):
            place[idx] = list(line)
        corona = False
        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P':
                    continue
                for k in range(12):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x < 0 or y < 0 or x >= 5 or y >= 5:
                        continue
                    if place[x][y] == 'P':
                        if k in [0, 1, 2, 3]:
                            answer.append(0)
                            corona = True
                            break
                        elif k in [4, 5, 6, 7]:
                            if place[i][y] != 'X' or place[x][j] != 'X':
                                answer.append(0)
                                corona = True
                                break
                        else:
                            if place[(i + x)//2][(j + y)//2] != 'X':
                                answer.append(0)
                                corona = True
                                break
                if corona:
                    break
            if corona:
                break
        if not corona:
            answer.append(1)
    return answer