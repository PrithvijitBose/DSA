class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        seen= {}

        for i in range(n):
            need = target - nums[i] #9-2 = 7

            if need in seen:
                return [seen[need],i]
            
            seen[nums[i]] = i # seen[2]=0 

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        