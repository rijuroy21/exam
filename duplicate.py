l=[1,2,3]
a=int(input("Enter a number"))
for i in l:
    if a not in l:
        l.append(a)
        print(l)
    else:
        print("duplicate values")
        break    