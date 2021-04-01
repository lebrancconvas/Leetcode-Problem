def twosum(nums, target):
    inarr = []
    for i in range(0, len(nums) - 1): 
        for j in range(i + 1, len(nums)):
            if(nums[i] + nums[j] == target):
                inarr.append(i)
                inarr.append(j)
    return inarr

print(twosum([2,7,11,15], 9))
print(twosum([3,2,4], 6))
print(twosum([3,3], 6))

