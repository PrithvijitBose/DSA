# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLL(self,head):
        prev= None
        curr = head

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev         
    def pairSum(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        p2 = self.reverseLL(slow)
        p1 = head
        maxi = float('-inf')

        while p1 != None and p2 != None:
            total = p1.val + p2.val
            maxi = max(total,maxi)
            p1 = p1.next
            p2 = p2.next
        return maxi

            


        
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        