l,n = [int(inp) for inp in input().split()]

s = input()
c=0
ans=0
a = input().split()
# a = "^["+"|".join(input().split())+"]"
# a = "^["+"|".join(["^["]+input().split()+["]"])+"]"
for i in s:
    if(i in a):
        c+=1
    else:
        # print((c*(c+1))//2)
        ans+=(c*(c+1))//2
        c=0
ans+=(c*(c+1))//2
print(ans)
