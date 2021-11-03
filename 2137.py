while 1:
    n = int(input())
    a = [" " for i in range(n)]
    for i in range(n):
        a[i] = input()
    a.sort()
    for i in range(n):
        print(a[i])
    if int(a[0])==0:
        break
