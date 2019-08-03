def twoSum(nums, target):
    hash_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_dict:
            return[hash_dict[target - nums[i]], i]
        else:
            hash_dict[nums[i]] = i
    return -1

test = [1, 3 ,6 ,9, 0]
target = 4

print(twoSum(test, target))

#Basic 2 sum using hashmap. O(N) in time