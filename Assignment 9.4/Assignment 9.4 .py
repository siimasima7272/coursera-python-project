name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
email = list()
counts = dict()

for line in fh:
    if not line.startswith('From'): continue
    tline = line.split()
    if len(tline) > 2: continue
    email.append(tline[1])

for sender in email:
    counts[sender] = counts.get(sender, 0) + 1

bigsender = None
mostmail = None
for ksender, vmail in counts.items():
    if mostmail is None or vmail > mostmail:
        mostmail = vmail
        mostsender = ksender

print(mostsender, mostmail)




