def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        prev = None
        def rev(head,prev):
            temp = head.next 
            head.next = prev
            if temp is None:
                return head
            else:
                return rev(temp,head)


        return rev(head,None)
