def middleNode(self, head: ListNode):
    if not head.next:
        return head
    fast=slow=head
    while fast and fast.next:
        fast,slow=fast.next.next,slow.next
    return slow