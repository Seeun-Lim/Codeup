a,b,c=map(int, input().split(" "))
sum=0

for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            sum+=1

print(sum)