class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # stk =[]
        if head is None or head.next is None:
            return True
        fast = head
        slow = head
        while fast.next != None and fast.next.next!= None:
            fast = fast.next.next
            # stk.append(slow.val)
            slow = slow.next
        slow.next = self.reverse(slow.next)
        slow = slow.next
        temp = head
        while slow!= None:
            if slow.val != temp.val:
                return False
            slow = slow.next
            temp = temp.next
              
        return True

        
    def reverse(self,ptr):
        pre = None
        next = None
        while ptr != None:
            next = ptr.next
            ptr.next = pre

            pre = ptr
            ptr = next
        return pre        
