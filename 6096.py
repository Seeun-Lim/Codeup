d=[]

def tenthreverse(d,x,y):
    for i in range(19):
        if d[x][i]==0:
            d[x][i]=1
        else:
            d[x][i]=0
    for i in range(19):
        if d[i][y]==0:
            d[i][y]=1
        else:
            d[i][y]=0

for i in range(19):
    temp=list(map(int,input().split()))
    d.append(temp)

n=int(input())

for i in range(n):
    x,y=map(int,input().split())
    tenthreverse(d,x-1,y-1)

for a in d:
    for b in a:
        print(b,end=' ')
    print()