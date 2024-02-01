def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevnode = None
        def kthNode(temp,k):
            k-=1
            while temp!= None and k>0:
                k-=1
                temp = temp.next
            return temp
        def reverse(head):
            temp = head
            prev = None
            while temp is not None:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            return prev



        while temp != None :
            knode = kthNode(temp,k)
            if knode is None:
                if prevnode != None:
                    prevnode.next = temp
                break
            nextnode = knode.next
            knode.next = None
            reverse(temp)

            if head == temp:
                head = knode
            else:
                prevnode.next = knode
            prevnode = temp
            temp = nextnode
        return head


# 25. Reverse Nodes in k-Group
# Solved
# Hard
# Topics
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
