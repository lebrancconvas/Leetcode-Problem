def twosum(nums, target):
    inarr = []
    for i in range(0, len(nums) - 1): 
        for j in range(i + 1, len(nums)):
            if(nums[i] + nums[j] == target):
                inarr.append(i)
                inarr.append(j)
    return inarr



