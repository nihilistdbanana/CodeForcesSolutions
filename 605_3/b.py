t = int(input())

for ts in range(t):
    s = list(input())
    l = len(s)
    f={}
    for i in s:
        f[i]=f.get(i,0)+1
    mlr = min(f.get("L",0),f.get("R",0))
    mud = min(f.get("U",0),f.get("D",0))

    if min(mlr,mud)>0:
        print(mlr*2+mud*2)
        print("U"*mud,"R"*mlr,"D"*mud,"L"*mlr, sep="")
    elif max(mlr,mud)>0:
        print(2)
        print("U"*min(mud,1),"R"*min(mlr,1),"D"*min(mud,1),"L"*min(mlr,1), sep="")
    else:
        print(0)
        print()
