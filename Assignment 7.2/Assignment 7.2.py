fname=input("enter your file name:")
fhandle=open(fname)
count=0
result=0
for line in fhandle:
    if not  line.startswith("X-DSPAM-Confidence:"):
       continue
    count=count + 1
    line=line.rstrip()
    x=line.find(":")
    y=line[x+2:]
    y=float(y)
    result= result + y
print('Average spam confidence:',result/count)

