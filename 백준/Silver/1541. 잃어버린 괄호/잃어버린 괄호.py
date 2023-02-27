mod=input()
if '-' in mod:
    mod2=mod[:mod.index('-')]
    mod=mod[mod.index('-')+1:]
    sum_mod2=0
    for i in list(mod2.split('+')):
        sum_mod2+=sum(map(int, i.split('-')))
    sum_mod=0
    for i in list(mod.split('+')):
        sum_mod+=sum(map(int, i.split('-')))
    print(sum_mod2-sum_mod)
else:
    print(sum(map(int, mod.split('+'))))