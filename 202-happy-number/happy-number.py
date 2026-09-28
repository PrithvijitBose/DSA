class Solution(object):
    def sumofSquareDigits(self,n):
        sums = 0
        # 36
        while n>0 :
            digit = n%10
            sums = sums+(digit*digit)
            n=n/10
        return sums
    def isHappy(self, n):
        slow=n
        fast=n

        while fast != 1:
            slow = self.sumofSquareDigits(slow)
            fast = self.sumofSquareDigits(self.sumofSquareDigits(fast))

            if fast == 1:
                return True
            
            if slow == fast:
                return False
        
        return True
    
        


        """
        :type n: int
        :rtype: bool
        """
        