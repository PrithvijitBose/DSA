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
        # length of linked list
        while l != None:
            leng = leng + 1
            l = l.next 


        d = leng - n # 5-2=3
        prev = dummy
        

        for _ in range(d):
            prev= prev.next
        prev.next = prev.next.next
        return dummy.next
