# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) :
        if not l1:return l2
        if not l2:return l1
        #head=ListNode(0)
        #copy=head
        copy=head=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
        #if not l1:
        #    head.next=l2
        #else:
        #    head.next=l1
        head.next=l1 or l2
        return copy.next
#recursive:
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
#
            