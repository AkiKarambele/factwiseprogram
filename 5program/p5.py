def nmd(gas , cost):
    tg=0
    cg=0
    s=0
    for i in range(len(gas)):
        tg+=gas[i]-cost[i]
        cg+=gas[i]-cost[i]
        if cg<0:
            cg=0
            s=i+1
    if tg>=0:
        return s
    else:
        -1
gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
print(nmd(gas,cost))

       