g1=input()
g2=len(g1)
g3=[]
for j in range (0,g2,2):
    g3.append(g1[j:j+2][::-1]) 
print("".join(g3))
