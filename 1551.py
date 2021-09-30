n = int(input())
while n:
    x = input()
    s = ''.join(filter(str.isalnum,x))
    lenth = len(set(s))
    if lenth==26:
        print("frase completa")
    elif lenth>=13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")    
    
    n-=1