n = int(input())
while n:
    str1 = input()
    str2 = input()
    val = 0
    for i in range(len(str1)):
        dif = ord(str2[i]) - ord(str1[i])
        if dif<0:
            dif = dif +26
        val = val + dif
    print(val) 
    n-=1  

