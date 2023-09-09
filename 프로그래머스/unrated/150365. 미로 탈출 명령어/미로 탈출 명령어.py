import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):
    answer = dfs(n, m, x, y, r, c, k, '')
    if not answer:
        answer = "impossible"
    return answer

def dfs(n, m, x, y, r, c, k, log):
    if k == 0:
        if x == r and y == c:
            return log
        return
    else:
        if abs(x-r) + abs(y-c) > k:
            return
        if (abs(x-r) + abs(y-c) - k) % 2:
            return "impossible"
        result = ''
        if x <= n - 1:
            result = dfs(n, m, x + 1, y, r, c, k - 1, log + 'd')
        if not result and y >= 2:
            result = dfs(n, m, x, y - 1, r, c, k - 1, log + 'l')
        if not result and y <= m - 1:
            result = dfs(n, m, x, y + 1, r, c, k - 1, log + 'r')
        if not result and x >= 2:
            result = dfs(n, m, x - 1, y, r, c, k - 1, log + 'u')
        if result:
            return result