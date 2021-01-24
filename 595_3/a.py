t = int(input())

for ts in range(t):
    l = int(input())
    a = [int(i) for i in input().split()]

    a.sort()
    f=1
    for i in range(1,l):
        if(a[i]-a[i-1]==1):
            f=2
            break
    print(f)
