# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if not l1 and not l2:return None 
        copy=result=ListNode(0)
        last=0
        while l1 or l2 or last:
            v1=v2=0
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2.l2.next
            ans=last+v1+v2
            last=ans//10
            result.next=ListNode(ans%10)
            result=result.next
        return copy.next
        