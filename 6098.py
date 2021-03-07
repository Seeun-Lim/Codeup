d=[]

for i in range(10):
    temp=list(map(int,input().split()))
    d.append(temp)

a = 1
b = 1

while True:
    if d[a][b] == 2:
        d[a][b]=9
        break
    elif d[a+1][b]==1 and d[a][b+1]==1:
        d[a][b]=9
        break

    d[a][b]=9

    if d[a+1][b]==1:
        b+=1
    elif d[a][b+1]==1:
        a+=1
    else: b+=1

for x in d:
    for y in x:
        print(y, end=' ')
    print()