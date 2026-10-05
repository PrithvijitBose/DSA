class Solution(object):
    def calcNextIdx(self,nums,curr):
        return (curr + nums[curr]) % len(nums)

    def circularArrayLoop(self, nums):
        # seq, k>1 , all positive or all negative
        # we should check for all indexes

        for i in range(len(nums)):
            # set -> indexes we have visited so far
            # flag -> isPos = nums[i]> 0
            # [2,-1,1,2,2]
            #  0
            # {0,2,3}

            if nums[i]==0:
                continue

            # Determine the direction of the loop (all positive or all negative)
            isPos = nums[i] > 0
            slow = i
            fast = i
            # cycle detection

            while True:
                slow = self.calcNextIdx(nums,slow)
                if (isPos and nums[slow] < 0) or (not isPos and nums[slow] > 0):
                    break
                fast = self.calcNextIdx(nums,fast)
                if (isPos and nums[fast] < 0) or (not isPos and nums[fast] > 0):
                    break 
                fast = self.calcNextIdx(nums,fast)
                if (isPos and nums[fast] < 0) or (not isPos and nums[fast] > 0):
                    break 

                if slow == fast:
                    #cycle
                    # k > 1
                    if slow != self.calcNextIdx(nums,slow):
                        return True
                    break

            curr = i

            if isPos:
                while nums[curr]>0:
                    nxt = self.calcNextIdx(nums,curr)
                    nums[curr] = 0

                    curr = nxt

            if not isPos:
                while nums[curr]<0:
                    nxt = self.calcNextIdx(nums,curr)
                    nums[curr] = 0

                    curr = nxt
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """
        