class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        i = 0
        j= n-1

        while i<j:
            total = numbers[i]+numbers[j]

            if total == target:
                return [i+1,j+1] 
            elif total > target:
                j-=1
            else:
                i+=1
        


        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        