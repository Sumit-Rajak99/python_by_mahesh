# num=int(input("enter any number: "))
# rv=1
# for i in range(1,num+1):
#     rv=rv*i
    
# print(rv)    

def rec(n):
    if n==1:
        return 1
    return n*rec(n-1)
print(rec(5))    
    
    
    