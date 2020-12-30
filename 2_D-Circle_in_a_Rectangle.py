w, h, x, y, r = (int(x) for x in input().split())
if x >= r and x <= w - r and y >= r and y <= h - r:
    print('Yes')
else:
    print('No')