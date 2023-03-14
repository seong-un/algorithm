import sys
import bisect
input=sys.stdin.readline

N=int(input())
Xi=list(map(int, input().split()))
sort_Xi=sorted(list(set(Xi)))

binary=[]
for idx, i in enumerate(Xi):
    Xi[idx]=bisect.bisect(sort_Xi, i)-1
    # start=0
    # end=len(sort_Xi)
    # while start<=end:
    #     mid=(start+end)//2
    #     if sort_Xi[mid]==i:
    #         print(idx)
    #         if idx>=1 and sort_Xi[idx-1]==i:
    #             end=mid-1
    #         else:
    #             Xi[idx]=mid
    #             break
    #     elif i<sort_Xi[mid]:
    #         end=mid-1
    #     else:
    #         start=mid+1
print(*Xi)