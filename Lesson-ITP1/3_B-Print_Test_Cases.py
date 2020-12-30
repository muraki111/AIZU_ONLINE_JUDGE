mylist = []
num = 1
for i in range(0, 10000):
    val = input()
    if val == "0":
        break
    if val:
        mylist.append(val)
for item in mylist:
    print("Case %d: %s" % (num, item))
    num+=1