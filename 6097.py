h,w=map(int,input().split())
n=int(input())

d=[[0] * w for _ in range(h)]

for i in range(n):
    l,e,x,y=map(int,input().split())
    for j in range(l):
        if(e==0):
            d[x-1][y-1+j]=1
        else:
            d[x-1+j][y-1]=1

for i in range(h):
    for j in range(w):
        print(d[i][j],end=' ')
    print()
