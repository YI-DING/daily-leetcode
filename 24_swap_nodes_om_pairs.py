class Solution:
    def swapPairs(self, head: ListNode) :
        if not head:
            return None 
        if not head.next:
            return head
        copy=ListNode(None)
        start,count=copy,0
        while head:
            count+=1
            if count == 1:
                previous=head
                head=head.next
            else:
                copy.next=head
                previous.next=head.next
                head.next=previous
                head=previous.next
                copy=previous
                count=0
        return start.next
#another great way:
class Solution:
    def swapPairs(self, head: ListNode) :
        #pre->first->second->  to  pre->second->first->
        if not head:
            return None 
        if not head.next:
            return head
        pre,pre.next=self,head
        while pre.next and pre.next.next:
            first=pre.next
            second=first.next
            pre.next,second.next,first.next=second,first,second.next
            pre=first
        return self.next