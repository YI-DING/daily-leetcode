'''class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None
     def __repr__(self):
     	return (f"node{self.val}")

one=ListNode(3)
two=ListNode(2)
third=ListNode(0)
fourth=ListNode(-4)

one.next=two
two.next=third
third.next=fourth
fourth.next=two'''

def detectCycle(head):
	if not head:return None
	fast=slow=head
	while fast and slow:
		fast=fast.next
		if fast is slow:break
		slow=slow.next
		if not fast:return None
		fast=fast.next
	fast=head
	slow=slow.next
	print(f'{fast},{slow}')
	while fast is not slow:
		print(f'{fast},{slow}')
		fast=fast.next
		slow=slow.next
	return(fast)
'''
answer=detectCycle(one)
print(f'answer is {answer}')
'''