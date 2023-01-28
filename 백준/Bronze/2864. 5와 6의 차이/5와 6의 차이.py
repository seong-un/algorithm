A,B=map(int, input().split())

if "5" in str(A) or "5" in str(B):
  maxA=str(A).replace("5", "6")
  maxB=str(B).replace("5", "6")
  maxAB=int(maxA)+int(maxB)
else:
  maxAB=A+B

if "6" in str(A) or "6" in str(B):
  minA=str(A).replace("6", "5")
  minB=str(B).replace("6", "5")
  minAB=int(minA)+int(minB)
else:
  minAB=A+B

print(minAB, maxAB)