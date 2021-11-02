n = int(input())
while n:
    strings = ["" for i in range(50)]

    i = 0
    maxL = 0
    store = n
    while n:

        strings[i] = input()
        if len(strings[i])>maxL:
            maxL = len(strings[i])

        i+=1
        n-=1
    for i in range(store):
        gap = maxL - len(strings[i])
        while gap:
            print(" ",end="")
            gap-=1
        print(strings[i])  
    n = int(input()) 