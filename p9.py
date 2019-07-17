bg1,bg2=input().split()
bg1=int(bg1)
bg2=int(bg2)
l=[]
if(bg1>1 and bgg2>1):
    for k in range (bg1,bg2+1):
        for t in range (2,k):
            if (k%t==0):
                break
        else:
            l.append(k)
print(len(l))
