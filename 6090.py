a,m,d,n=map(int, input().split(" "))

i=1
while(True):
    if(i==n):
        break
    else:
        i+=1
        a=a*m+d

print(a)