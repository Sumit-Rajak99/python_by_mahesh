def insertionsrt(nums):
    n=len(nums)
    count=0
    for i in range(1,n):
        j=i
        while j>0 and nums[j]<nums[j-1]:
            count=count+1
            t=nums[j]
            nums[j]=nums[j-1]
            nums[j-1]=t
            j=j-1
    print(count)
    return nums
print(insertionsrt([1,2,5,4,3]))        