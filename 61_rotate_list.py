class Solution:
    def rotateRight(self, head: ListNode, k: int):
        if not head or not head.next:
            return head
        lst=[]
        while head:
            lst.append(head)
            head=head.next
        length=len(lst)
        k%=length
        lst[length-1].next=lst[0]
        lst[length-1-k].next=None
        return lst[length-k] if k>0 else lst[0]
#Best version:
def rotateRight(self, head: ListNode, k: int):
    if not head:
        return None 
    pointer,length=head,1
    while head.next:
        length,head=length+1,head.next
    k%=length
    head.next=pointer
    for _ in range(length-k-1):
        pointer=pointer.next
    result=pointer.next
    pointer.next=None
    return result