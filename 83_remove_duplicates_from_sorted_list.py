# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head:return head
        copy=head
        while True:
            if not head or not head.next:break
            while head.next:
                if head.val==head.next.val:
                    head.next=head.next.next
                else:break
            head=head.next
        return copy
        