n,m = list(map(int,input().split()))
rl = []
ll = []
for _ in range(n):
    t = list(map(int,input().split()))
    ll.append(t)
for _ in range(n):
    t = list(map(int,input().split()))
    rl.append(t)
for l in ll:
    r = list(map(int,input().split()))
    for i in zip(l,r):
        print(sum(i),end = ' ')
    print()