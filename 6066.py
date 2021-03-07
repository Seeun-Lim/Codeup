list=[0,0,0]
list[0],list[1],list[2]=map(int,input().split(" "))

for i in range(3):
    if(list[i]%2==0):
        print("even")
    else:
        print("odd")