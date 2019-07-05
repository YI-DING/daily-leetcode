class Solution:
    def partition(self, head: ListNode, x: int):
        if not head or not head.next:
            return head
        result,result.next=self,head
        fast,slow,fast_pre,slow_pre,large_flag=head,head,self,self,False 
        while fast:
            if not large_flag:#large or equal val not found
                if fast.val < x:
                    slow,slow_pre=slow.next,slow_pre.next
                else:
                    large_flag=True
                fast,fast_pre=fast.next,fast_pre.next
            else:#slow has been settled
                if fast.val < x:
                    temp=fast.next
                    slow_pre.next=fast
                    fast.next=slow
                    slow_pre=slow_pre.next
                    
                    fast_pre.next=temp
                    fast=temp
                else:
                    fast,fast_pre=fast.next,fast_pre.next
        return result.next
#best way is to get a small link and larget link and finally connect them together
def partition(self, head, x):
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)
    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    l2.next = None
    l1.next = h2.next
    return h1.next