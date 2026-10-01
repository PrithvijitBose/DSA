# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseLL(self, head):
        # Your linked list reversal logic goes here
        prev = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        # 1 -> 2 -> 3 -> 4
        # 1 -> 2 -> 4 -> 3
        p2 = self.reverseLL(slow)  #
        p1 = head
        
        while p1 != None and p2 != None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
