a,d,n=map(int, input().split(" "))

i=1
while(True):
    if(i==n):
        break
    else:
        i+=1
        a*=d

print(a)