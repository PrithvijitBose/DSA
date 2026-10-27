class Solution(object):
    def findMaxAverage(self, nums, k):
        
        n = len(nums)
        left = 0
        sums = 0

        for right in range(k):
            sums += nums[right]
        
        max_average = sums
        
        for i in range(k,n):
            sums = sums + nums[i] - nums[i - k] 

            max_average = max(max_average,sums)

        return max_average/float(k)


   
        





        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        