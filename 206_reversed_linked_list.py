# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#iterative:
class Solution:
    def reverseList(self, head: ListNode):
        if not head:return head
        newtail=ListNode(head.val)
        newtail.next=None
        while head.next:
            nexx=ListNode(head.next.val)
            nexx.next=newtail
            newtail=nexx
            head=head.next
        return newtail

