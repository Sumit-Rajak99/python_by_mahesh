l=[-11,11,-98,4,3,-1]
ans=[]
size=len(l)
k=3
for i in range(size-k+1):
    n=0
    for j in range(i,i+k):
        if l[j]<0:
            # print(j,end=" ")
            n=l[j]
            break
    ans.append(n)
print(ans)        