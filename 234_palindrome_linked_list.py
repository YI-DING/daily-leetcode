'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
A,B,C,D,E=ListNode(1),ListNode(2),ListNode(3),ListNode(2),ListNode(1)
A.next,B.next,C.next,D.next=B,C,D,E

def isPalindrome(head: ListNode):
    if not head or not head.next:
        return True
    
    fast,slow,fast.next,slow.next=ListNode("ha"),ListNode("ha"),head,head
    odd_flag=False
    prev=None
    #find mid point and modify first half
    while fast and slow:
        print(fast.val,slow.val)
        nex=slow.next
        fast,slow.next=fast.next,prev
        prev=slow
        if not fast:
            break
        if not fast.next:
            odd_flag=True
            break
        fast=fast.next
        slow=nex
        print(fast.val,slow.val)
    head.next=None
    #start checking
    right=nex
    print(f'odd_flag is {odd_flag}')
    while right and slow:
        print(f'right is {right.val}, slow is {slow.val}')
        if right.val != slow.val:
            return False
        else:
            right,slow=right.next,slow.next
    return True

print(isPalindrome(A))
'''
def isPalindrome(self, head: ListNode) :
    if not head or not head.next:
        return True
    fast=slow=head
    prev=None
    #find mid
    while fast and fast.next:
        fast,slow,slow.next,prev=fast.next.next,slow.next,prev,slow
    slow=slow.next if fast else slow
    while prev and prev.val == slow.val:
        slow,prev=slow.next,prev.next
    return not prev