try:
  while True:
    N=int(input())
    Nbar=list("-"*(3**N))
    
    def bar(B):
      if len(B)==1:
        return B
      B[int(len(B)/3):int(len(B)/3*2)]=[" "]*(int(len(B)/3))
      B[0:int(len(B)/3)]=bar(B[0:int(len(B)/3)])
      B[int(len(B)/3*2):len(B)]=bar(B[int(len(B)/3*2):len(B)])
      return B
    
    print(*bar(Nbar), sep="")
except:
  pass