def inorder(n):
    global i
    if n > N:
        return
    inorder(2 * n)
    string[i] = tree[n]
    i+=1
    inorder(2 * n + 1)


for test_case in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(N):
        node, alphabet, *left = input().split()
        tree[int(node)] = alphabet
    string = [0] * N
    i=0
    inorder(1)
    print(f'#{test_case} ', *string,sep='')
