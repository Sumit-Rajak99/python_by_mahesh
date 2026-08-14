n=int(input("enter any number"))
sum=0
while n>0:
    digit=n%10
    if digit%2!=0:
        sum=sum+digit
        print(sum)
    n=n//10
print(sum)        