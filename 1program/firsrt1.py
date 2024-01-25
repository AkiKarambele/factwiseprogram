



num=[]
#num= list(map(int, input.split()))
n=int(input())
for i in range(n):
    num.append(int(input()))
n=[]
for i in num:
    if i not in n:
        n.append(i)

print(n)