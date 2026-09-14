# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        #n-2+5
        dummy = ListNode(0)
        dummy.next = head

        leng = 0
        l = head
        while l != None:
            leng = leng + 1
            l = l.next
        d = leng - n + 1

        prev = dummy
        curr = head
        
        # 0 1 2 3 4 5
        #       p c
        # d = 4
        i = 0
        while i < d -1:
            curr = curr.next
            prev= prev.next
            i+=1
        prev.next = prev.next.next
        return dummy.next
