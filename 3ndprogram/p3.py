
def nmd(num):
    min=0
    profit=0
    for j in num:
        if j < min:
            min =j
        elif profit< j-min:
            profit= j-min
    return profit

num=[7,1,5,3,6,4]
#num= list(map(int, input.split(,)))

min=0
profit=0
for j in num:
    if j < min:
        min =j
    elif profit< j-min:
        profit= j-min
print(nmd(num))
    