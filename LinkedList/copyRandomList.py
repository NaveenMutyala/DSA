# with map / dictionary
# 138. Copy List with Random Pointer
# Solved
# Medium
# Topics
# Companies
# Hint
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:



# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None :
            return head
        di = {}
        temp = head
        while temp != None:
            copyNode = Node(temp.val)
            di[temp] = copyNode
            temp = temp.next
        temp = head
        while temp != None:
            di[temp].next = di[temp.next] if temp.next else None
            di[temp].random = di[temp.random] if temp.random else None
            temp = temp.next
        return di[head]

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp != None:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next
        temp = head
        while temp != None:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        dummy = Node(-1)
        res = dummy
        temp = head
        while temp!= None:
            dummy.next = temp.next
            temp.next = temp.next.next
            dummy = dummy.next
            temp = temp.next
        return res.next
