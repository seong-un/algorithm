len_colored_paper=int(input())
papers=[]
for i in range(len_colored_paper):
    papers.append(list(map(int, input().split())))
colored_papers=[set() for i in range(len_colored_paper)]
for idx, paper in enumerate(papers):
    for i in range(paper[0], paper[0]+10):
        for j in range(paper[1], paper[1]+10):
            colored_papers[idx].add((i,j))
union_paper=set()
for i in colored_papers:
    union_paper=union_paper|i
print(len(union_paper))