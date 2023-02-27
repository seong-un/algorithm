mod=input()
if '-' in mod:
    mod2=mod[:mod.index('-')]
    mod=mod[mod.index('-')+1:]
    sm=0
    for i in list(mod2.split('+')):
        sm+=sum(map(int, i.split('-')))
    for i in list(mod.split('+')):
        sm-=sum(map(int, i.split('-')))
    print(sm)
else:
    print(sum(map(int, mod.split('+'))))