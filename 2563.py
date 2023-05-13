판때기 = [[0 for i in range(101)] for _ in range(101)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        판때기[y+i][x:x+10] = [1] * 10
ans = 0
for y in range(1,100):
    for x in range(1,100):
        if 판때기[y][x] == 1:
            ans += 1
print(ans)