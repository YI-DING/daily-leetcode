# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast=slow=head
        while fast and slow:
            fast=fast.next
            if fast==slow:return True 
            slow=slow.next
            if not fast:return False
            fast=fast.next
        return False 
