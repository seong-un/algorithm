str1=list(input())
str2=list(input())
LCS=[0]*len(str1)
first=0
for j in range(len(str2)):
    pre_LCS=LCS[:]
    for i in range(len(str1)):
        if i==0:
            if str1[i]==str2[j]:
                first=1
        LCS[0]=first
        if str1[i]==str2[j]:
            LCS[i]=pre_LCS[i-1]+1
        else:
            LCS[i]=max(pre_LCS[i], LCS[i-1])
print(LCS[-1])