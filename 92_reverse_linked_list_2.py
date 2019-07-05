class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        if not head or not head.next or m == n:
            return head
        result,result.next,count=self,head,0
        prev=result
        while head:
            count+=1
            if count == m:
                start=prev
                end=head
                prev=head
                head=head.next
            elif m < count <= n:
                if head.next:
                    temp=head.next
                    head.next=prev
                    prev=head
                    head=temp
                else:
                    start.next=head
                    head.next=prev
                    end.next=None
                    break
            elif count == n+1:
                start.next=prev
                end.next=head
                head=head.next
            else:
                prev,head=head,head.next
        return result.next
#cleaner code:
#same idea, without a counting variable
#use for loop to skip the parts outside [m,n]
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
#note that using start and end instead of pre.next and pre.next.next is more clear 