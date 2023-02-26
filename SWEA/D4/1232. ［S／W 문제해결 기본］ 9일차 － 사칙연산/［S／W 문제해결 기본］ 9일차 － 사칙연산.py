def postorder(n):
    if tree[n-1][1]=='+':
        return postorder(int(tree[n-1][2]))+postorder(int(tree[n-1][3]))
    elif tree[n-1][1]=='-':
        return postorder(int(tree[n-1][2]))-postorder(int(tree[n-1][3]))
    elif tree[n-1][1]=='*':
        return postorder(int(tree[n-1][2]))*postorder(int(tree[n-1][3]))
    elif tree[n-1][1]=='/':
        return postorder(int(tree[n-1][2]))/postorder(int(tree[n-1][3]))
    else:
        return int(tree[n-1][1])

for t in range(1, 11):
    N=int(input())
    tree=[0]*N
    for i in range(N):
        tree[i]=list(input().split())
    print(f'#{t} {int(postorder(1))}')