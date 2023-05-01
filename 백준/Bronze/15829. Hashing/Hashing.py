L=int(input())
string=input()
total=0
for idx, i in enumerate(string):
    total+=(ord(i)-96)*31**idx
print(total)