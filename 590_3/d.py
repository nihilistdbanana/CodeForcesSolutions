s = list(input())
q = int(input())
ind = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[], "h":[], "i":[], "j":[], "k":[], "l":[], "m":[], "n":[], "o":[], "p":[], "q":[], "r":[], "s":[], "t":[], "u":[], "v":[], "w":[], "x":[], "y":[], "z":[]}

for i in range(len(s)):
    ind[s[i]].append(i)

for i in range(q):
    c,f,l = input().split()
    c=int(c)

    if c == 1:
        f = int(f)-1
        ind[s[f]].remove(f)
        ind[l].append(f)
        s[f]=l
    else:
        # print(set(s[l-1:f]))
        f = int(f)
        l = int(l)
        # print(list(set(s[l-1:f])))
        # print(s[f-1:l])
        c = 0
        for i in list(ind.values()):
            if(any((x>=f-1 and x<l) for x in i)):
                    c+=1
        print(c)
