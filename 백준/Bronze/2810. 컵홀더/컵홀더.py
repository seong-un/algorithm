N=int(input())
seat=list(input())

try:
  for i in range(len(seat)-1):
    if seat[i]=="L":
      seat.insert(i, seat[i]+seat[i+1])
      del seat[i+1:i+3]
except:
  pass

for i in range(len(seat)+1):
  seat.insert(2*i, "*")

if "LL" in seat:
  print(seat.count("*"))
else:
  print(seat.count("*")-1)