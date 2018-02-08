def twoSum(nums, target):
    keys = {}
    for i in xrange(len(nums)):
        if nums[i] not in keys:
            keys[nums[i]] = i
        if target - nums[i] in keys:
            print [keys[target - nums[i]], i]

twoSum([2,1,2,34,8,5,65,6,7,11,17], 9)