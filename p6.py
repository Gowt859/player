g1,g2=map(str,input().split())
for j in range(len(g1)):
    if(g1.count(g1[j])==g2.count(g2[j])):
        print('yes')
        break
    else:
        print('no')
        break
