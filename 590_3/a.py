import math
t = int(input())


for ts in range(t):
    l = int(input())
    print(math.ceil(sum([int(i) for i in input().split()])/l))
