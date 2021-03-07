n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
    if(i==0):
        min=a[0]
    else:
        if(min>=a[i]):
            min=a[i]

print(min)
