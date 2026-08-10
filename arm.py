num=int(input("enter any number:"))
count=0
x=y=num
sum=0
while num>0:
    count=count+1
    num=num//10
while x>0:
    lastdigit=x%10  
    sum=sum+lastdigit**count
    x=x//10
if y==sum:
    print(f'{y} is armstrong')
else:
    print(f'{y} is not armstrong')      
