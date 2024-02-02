def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        n = 1
        temp = head
        while temp.next!=None:
            n+=1
            temp = temp.next
        temp.next = head
        k = k%n
        end = n-k
        while end !=0:
            end-=1
            temp = temp.next
        head = temp.next
        temp.next = None
        return head
# 61. Rotate List
# Solved
# Medium
# Topics
# Companies
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
