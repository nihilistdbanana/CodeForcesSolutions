t = int(input())


for ts in range(t):
    l = int(input())
    a = [(int(i)>=3) for i in list(input())]
    # print(a)
    a = [a,[(int(i)>=3) for i in list(input())]]
    w = 0
    for i in range(l):
        # print(a[0][i] and a[1][i], a[w][i], a[(w+1)%2][i],w , end="-->")
        if(a[0][i] and a[1][i]):
            w=(w+1)%2
        elif a[w][i]:
            w = 0
            break
        # print(w)
    if w == 0:
        print("NO")
    else:
        print("YES")
