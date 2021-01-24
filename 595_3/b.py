t = int(input())

for ts in range(t):
    l = int(input())
    a = [int(i) for i in input().split()]
    aa = a
    c=[]
    for i in range(l):
        if(a[i]!=0):
            nx = i
            cc=[]
            while(a[nx]!=0):
                # print(nx, end = " ")
                cc.append(nx)
                t = a[nx]-1
                a[nx] = 0
                nx = t
                # print(nx,a[nx]!=0)
            c.append(cc)
    # print(c)
    for i in c:
        ll = len(i)
        for j in i:
            a[j]=ll
    for i in a:
        print(i, end=" ")
    print()
