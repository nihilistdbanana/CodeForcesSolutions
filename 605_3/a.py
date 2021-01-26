t = int(input())

for ts in range(t):
    a,b,c = [int(i) for i in input().split()]
    print(max(0,abs(a-b)+abs(a-c)+abs(c-b)-4))
