# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next

            if slow == fast:

                break
        if fast == None or fast.next == None:
            return None
        

        n1 = slow
        n2 = head

        while n1 != n2:
            n1 = n1.next
            n2 = n2.next
        return n1
        """
        :type head: ListNode
        :rtype: ListNode
        """
        