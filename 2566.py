m = []
for _ in range(9):
    m.append(list(map(int,input().split())))
ans = m[0][0]
x = 0
y = 0
mx = 0
for i in range(9):
    for j in range(9):
        if ans < m[i][j]:
            ans = m[i][j]
            x = j+1
            y = i+1
print(ans)
print(y,x)