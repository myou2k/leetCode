#46 Permutations: https://leetcode.com/problems/permutations/

def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #Generate all possible permutations using DFS
    #O(n*n!) -> O(n!)
    
    numSet = set(nums)
    currRes = []
    res = []
    def helper(currRes, currSet, res):
        if currSet:
            for num in currSet:
                temp = currSet.copy()
                temp.remove(num)
                helper(currRes + [num], temp, res)
        else: 
            res.append(currRes)
    helper(currRes, numSet, res)
    return res

'''
Revisited using backtracking algo
Choices: Given a partial permutation, append the next digit
Constraints: Is a permutation
Goal: Complete Permutation and backtrack
'''
def permute(self, nums: List[int]) -> List[List[int]]:
    permutations = []
    partial = []
    def helper(permutations, partial, nums):
        if len(partial) == len(nums):
            permutations.append(partial.copy())
        else:
            for i in range(len(nums)):
                if nums[i] in partial: # O(n) runtime
                    continue
                partial.append(nums[i])
                helper(permutations, partial, nums)
                partial.pop()
    helper(permutations, partial, nums)
    return permutations