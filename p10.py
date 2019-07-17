g1,c1=input("").split()
s=list(g1)
b=list(c1)
count=0
for i in range(0,len(s)):
  if(s[i]!=b[i]):
    count+=1
if(count==1):
  print("yes")
else:
    print("no")
