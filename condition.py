l=[1,2,-3,4,-5,9]

ans=0
sum=0
dec=0
for i in l:
    if i>=1:
        sum=sum+i
    else:
        ans=sum-i 
        sum=0
        
print(ans)           
