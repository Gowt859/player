a1,b1 = map(int,input().split())
for i in range(max(a1,b1), a1*b1+1) :
    if (i%a1 == 0) and (i%b1 == 0) :
        ans = i
        break
print(ans)
