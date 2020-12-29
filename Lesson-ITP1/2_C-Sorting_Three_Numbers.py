a, b, c = (int(x) for x in input().split())
if a < b:
    if a < c:
        if b < c:
            print(a, b, c)
        else:  #b > c
            print(a, c, b)
    else:  #a > c
        if b > c:
            print(c, a, b)
else:  #a > b
    if a < c:
        if b < c:
            print(b, a, c)
    else:  #a > c
        if b < c:
            print(b, c, a)
        else:
            print(c, b, a)