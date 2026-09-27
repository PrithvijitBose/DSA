class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        i = 0
        j= n-1
        k=0

        while i<=j:
            if nums[i] > 1:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
            elif nums[i]< 1:
                nums[k],nums[i]=nums[i],nums[k]
                i+=1
                k+=1
            else:
                i+=1

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        