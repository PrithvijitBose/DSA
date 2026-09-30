class Solution(object):
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        while True:
            slow = nums[slow] # slow = nums[0] = 1
            fast = nums[nums[fast]] # fast = nums[nums[0]] = nums[1] = 3

            if slow == fast:
                break
        
        slow = 0  # Reset one pointer to the start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    

        """
        :type nums: List[int]
        :rtype: int
        """
        