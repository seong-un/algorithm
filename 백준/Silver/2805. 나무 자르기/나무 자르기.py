N, M=map(int, input().split())
tree=list(map(int, input().split()))

tree.sort(reverse=True)
start=0
end=max(tree)
def treecut(x):
  global start, end
  sum_tree=0
  for i in range(len(tree)):
    if tree[i]-x<=0:
      break
    sum_tree+=tree[i]-x
  if sum_tree<M:
    del sum_tree
    if end==x:
      return x
    end=x
    return treecut((start+x)//2)
  elif sum_tree>M:
    del sum_tree
    if start==x:
      return x
    start=x
    return treecut((x+end)//2)
  else:
    return x

print(treecut((max(tree))//2))