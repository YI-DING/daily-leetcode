def reorderList(head: ListNode) :
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        #find length and positions
        copy,count=head,0
        while copy:
            count,copy=count+1,copy.next
        cutoff=(count+1)//2
        #first_tail,second_head
        copy=head
        for _ in range(cutoff-1):
            copy=copy.next
        first_tail,second_head,first_tail.next=copy,copy.next,None
        #reverse second half
        cur=second_head.next
        second_head.next=None
        for _ in range(count-cutoff-1):
            temp=cur.next
            cur.next=second_head
            second_head=cur
            cur=temp
        #insert
        while head and second_head:
            fst=head.next
            head.next,snd=second_head,second_head.next
            second_head.next=fst
            head,second_head=fst,snd

