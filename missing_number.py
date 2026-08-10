# def missingNumber(nums):
#     n = len(nums)
#     return n*(n+1)//2 - sum(nums)

def missingNumber(num):
    n = len(num) + 1   
    total = n * (n + 1) // 2
    return total - sum(num)

num = [1,2,3,4,6,7,8,9]
print(missingNumber(num))