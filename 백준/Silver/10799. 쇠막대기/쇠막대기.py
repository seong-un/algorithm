iron=input()
iron=iron.replace('()', '/')
cnt=0
result=0
for i in iron:
    if i=='(':
        cnt+=1
    elif i=='/':
        result+=cnt
    else:
        cnt-=1
        result+=1
print(result)