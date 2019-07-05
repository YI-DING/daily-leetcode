class Solution:
    def removeElements(self, head: ListNode, val: int) :
        if not head:
            return None 
        if not val:
            return head
        result,result.next=self,head
        prev=result
        while head:
            if head.val == val:
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return result.next