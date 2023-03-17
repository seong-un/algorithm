N=int(input())
pre_round='A'
mid_round='A'
post_round='A'
for i in range(N):
    node=list(input().split())
    pre_round=pre_round.replace(node[0], ''.join(node))
    mid_round=mid_round.replace(node[0], node[1]+node[0]+node[2])
    post_round=post_round.replace(node[0], node[1]+node[2]+node[0])
print(pre_round.replace('.', ''))
print(mid_round.replace('.', ''))
print(post_round.replace('.', ''))