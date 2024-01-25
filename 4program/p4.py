def nmd(num,tar):
    low,hi=0,len(num)-1
    while low<=high:
        m=(low+hi)//2
        if num[m]==tar:
            return mid
        elif num[m] < tar:
            low=m+1
        else:
            hi=m-1

    return low


num=[1,2,3,4]

print(nmd(num,3))


