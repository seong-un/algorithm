import math

N_switch=int(input())
switch=list(map(int, input().split()))
N_student=int(input())
students=[0]*N_student
for i in range(N_student):
    students[i]=list(map(int, input().split()))
for student in students:
    if student[0]==1:
        for i in range(student[1]-1, len(switch), student[1]):
            switch[i]=abs(switch[i]-1)
    else:
        i=1
        switch[student[1]-1]=abs(switch[student[1]-1]-1)
        try:
            while student[1]-i-1>=0:
                if switch[student[1]-i-1]==switch[student[1]+i-1]:
                    switch[student[1]-i-1]=abs(switch[student[1]-i-1]-1)
                    switch[student[1]+i-1]=abs(switch[student[1]+i-1]-1)
                    i+=1
                else:
                    break
        except:
            pass
for i in range(math.ceil(len(switch)/20)):
    print(*switch[i*20:(i+1)*20])