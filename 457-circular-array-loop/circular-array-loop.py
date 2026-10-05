class Solution(object):
    def calcNextIdx(self,nums,curr):
        return (curr + nums[curr]) % len(nums)

    def circularArrayLoop(self, nums):
        # seq, k>1 , all positive or all negative
        # we should check for all indexes

        for i in range(len(nums)):
            # set -> indexes we have visited so far
            # flas -> isPos = nums[i]> 0
            # [2,-1,1,2,2]
            #  0
            # {0,2,3}

            if nums[i]==0:
                continue
            visited = set()
            visited.add(i)

            # Determine the direction of the loop (all positive or all negative)
            isPos = nums[i] > 0
            curr = i
            # cycle detection

            while True:
                nxt = self.calcNextIdx(nums,curr)

                if isPos and nums[nxt]< 0:
                    break
                if not isPos and nums[nxt] > 0:
                    break
                    
                # Cycle detection
                if nxt in visited:
                    # A valid loop must have a length k > 1 (cannot loop back to itself immediately)
                    if curr != nxt:
                        return True
                    else:
                        break
                visited.add(nxt)
                curr = nxt
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
        