class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) :
        if not head:
            return None 
        lst,copy=[],head
        while head:
            lst.append(head)
            head=head.next
        length=len(lst)
        if n==length:
            return copy.next
        elif n==1:
            lst[length-2].next=None
        else:
            lst[length-n-1].next=lst[length-n+1]
        return copy