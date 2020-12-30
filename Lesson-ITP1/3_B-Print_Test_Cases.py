mylist = []
num = 1
for i in range(0, 10000):
    val = input()
    if val:
        mylist.append(val)
    if val == "0":
        break
for item in mylist:
    print("Case %d: %s" % (num, item))
    num+=1