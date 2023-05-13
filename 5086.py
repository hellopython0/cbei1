while True:
    a,b = list(map(int,input().split()))
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
    if a==b==0:
        break