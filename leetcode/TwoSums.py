def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        x = target - num
        if x in seen:
            return [seen[x], i]
        seen[num] = i

nums = [3, 4, 5, 1, 6, 7]
target = 4
print(twoSum(nums, target))
