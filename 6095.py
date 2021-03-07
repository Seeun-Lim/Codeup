n=int(input())
d=[]

for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)

for i in range(n):
    a,b=map(int,input().split())
    d[a-1][b-1]=1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()
