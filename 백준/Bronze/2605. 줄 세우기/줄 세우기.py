N=int(input())
numbers=list(map(int, input().split()))
line=[]
for idx, i in enumerate(numbers):
        line.insert(len(line)-i, idx+1)
print(*line)