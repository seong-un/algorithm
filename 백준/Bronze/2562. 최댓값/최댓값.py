number=int(input())
idx=1
for i in range(8):
  number2=int(input())
  if number<number2:
    number=number2
    idx=i+2
print(number, idx, sep='\n')