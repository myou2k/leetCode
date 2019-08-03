class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Brute force is to recursively find all combinations and return the max
        '''
        def helper(nums, i):
            if i < 0:
                return 0
            else:
                return max(helper(nums, i-1), helper(nums, i-2) + nums[i])
        return helper(nums, len(nums) - 1)
        '''
        #Using memoization we can reduce runtime by cahcheing combination we have     already solved. "Top down"
        '''
        if len(set(nums)) == 1 and 0 in set(nums): #Timing out on [0,0,0,0,.....,0]
            return 0
        memo = [-1]*len(nums)
        def helper(nums, i):
            if i < 0:
                return 0
            if memo[i] > 0:
                return memo[i]
            else:
                res = max(helper(nums, i-1), helper(nums, i-2) + nums[i])
                memo[i] = res
                return res
        return helper(nums, len(nums) - 1)
        '''
        
        #Tabulation we build an array that keep track of maxmimum money that can be stolen so far "Bottom up"
        '''
        if len(nums) == 0:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        for i in range(len(nums)):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])
        return dp[-1]
        '''
        
        #We actually don't need the table since we only need the element after and before
        if len(nums) == 0: #Isn't needed
            return 0
        res = 0
        prev = 0
        prevprev = 0
        for i in range(len(nums)):
            res = max(prevprev + nums[i], prev)
            prevprev = prev
            prev = res
        return prev