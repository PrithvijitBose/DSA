class Solution(object):
    def sortedSquares(self, nums):
        n= len(nums)
        result = []
        i=0
        j=n-1


        while i<=j:
            m = abs(nums[i])
            p=abs(nums[j])

            if m>p:
                result.append(nums[i]*nums[i])
                i+=1
            else:
                result.append(nums[j]*nums[j])
                j-=1

        return result[::-1]
            




        """
        :type nums: List[int]
        :rtype: List[int]
        """
        