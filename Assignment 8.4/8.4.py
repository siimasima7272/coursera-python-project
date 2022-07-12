fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.split()
    for i in words:
        if not i in lst:
            lst.append(i)
    lst.sort()
print(lst)
