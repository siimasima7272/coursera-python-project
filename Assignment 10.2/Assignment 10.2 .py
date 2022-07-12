name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
lst = list()
hlst = list()
for line in handle:
    if not line.startswith('From'): continue
    tline = line.split()
    if len(tline) < 3: continue
    lst.append(tline[5])
    lst.sort()

for time in lst:
    hour = time.split(':')
    hlst.append(hour[0])
for i in hlst:
    count[i] = count.get(i, 0) + 1
for key, val in count.items():
    print(key, val)



