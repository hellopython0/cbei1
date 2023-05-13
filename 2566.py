n = 25
s = set
for i in range(1,n+1//2):
    if n % i == 0:
        s.add(i)
        s.add(n//i)
print(*s)