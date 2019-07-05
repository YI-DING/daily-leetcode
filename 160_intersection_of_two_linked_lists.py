class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None 
        cpyA,cpyB,lenA,lenB=headA,headB,0,0
        while cpyA:
            lenA,cpyA=lenA+1,cpyA.next
        while cpyB:
            lenB,cpyB=lenB+1,cpyB.next
        if lenA > lenB:
            for _ in range(lenA-lenB):
                headA=headA.next
        elif lenA < lenB:
            for _ in range(lenB-lenA):
                headB=headB.next
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA,headB=headA.next,headB.next
        return None