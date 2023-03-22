import sys
from collections import deque
sys.setrecursionlimit(10**9)

def input(): return sys.stdin.readline().rstrip()


def pre_order(i_s, i_e, p_s, p_e):
    if i_e - i_s == 1:
        if inorder[i_s] != postorder[p_s] or inorder[i_e] != postorder[p_e]:
            result.append(postorder[p_e])
            result.append(postorder[p_s])
        else:
            result.append(inorder[i_e])
            result.append(inorder[i_s])
        return
    if i_e - i_s == 0:
        result.append(inorder[i_e])
        return

    x = dct[postorder[p_e]]
    result.append(postorder[p_e])
    if x > i_s:
        pre_order(i_s, x - 1, p_s, p_s + x - i_s - 1)
        
    if x < i_e:
        pre_order(x + 1, i_e, p_e - (i_e - x), p_e - 1)


n = int(input())
inorder = list(map(int, input().split()))
dct = dict()
for idx, num in enumerate(inorder):
    dct[num] = idx
    
postorder = list(map(int, input().split()))

result = deque()
pre_order(0, n - 1, 0, n - 1)
print(*result)
