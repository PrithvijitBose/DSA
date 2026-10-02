# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        result = []

        curr = head

        while curr != None:
            result.append(curr.val)
            curr = curr.next
        
        # result = [5,4,2,1]
        i = 0
        j = len(result)-1
        maxi = float('-inf')

        while i<j:
            total = result[i]+result[j] #4+2 = 6
            maxi = max(total,maxi) # 6 , 6 = 6
            i+=1
            j-=1
        return maxi

            


        
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        