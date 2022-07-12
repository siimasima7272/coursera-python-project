import re
name=input("Enter your file name:")
fhand=open(name)
ls=list()
for line in fhand:
    num=re.findall('[0-9]+',line)
    if len(num)==0 :continue
    for i in num:
        ls.append(int(i))
print(sum(ls))
