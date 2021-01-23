n,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
onsc = set()
c = 0
chat = []
for i in a:
    # if i in chat:
    if i in onsc:
        continue
    else:
        chat.append(i)
        c+=1
        onsc.add(i)
        if c>k:
            c==k
            onsc.remove(chat.pop(0))
            # chat.pop(0)

print(len(chat))
for i in chat[::-1]:
    print(i,end=" ")

print()
