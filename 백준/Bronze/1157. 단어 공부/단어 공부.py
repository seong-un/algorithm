string=input().upper()
mx=0
alphabet=''
st=set(list(string))
for s in st:
  a=string.count(s)
  if mx<a:
    mx=a
    alphabet=s
  elif mx==a:
    alphabet='?'
print(alphabet)