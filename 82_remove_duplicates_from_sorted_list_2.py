class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head:
            return None 
        sett,flag,copy=set(),set(),head
        pre,pre.next=self,head
        while head:
            if head.val not in sett:
                sett.add(head.val)
            else:
                flag.add(head.val)
            head=head.next
        while copy:
            if copy.val in flag:
                pre.next=copy.next
            else:
                pre=copy
            copy=copy.next
        return self.next
#note that is one is not in place and does not use the info of 'sorted'.
#Best version:
def deleteDuplicates(self, head):
    dummy = pre = ListNode(0)
    dummy.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next
    return dummy.next