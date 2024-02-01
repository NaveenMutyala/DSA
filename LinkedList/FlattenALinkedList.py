def mergeList(a,b):
    temp = Node(val=0)
    res = temp
    while a != None and b!= None:
        if a.data <b.data:
            temp.child = a
            a = a.child
            temp = temp.child
        else:
            temp.child = b
            b = b.child
            temp = temp.child
    if a:
        temp.child = a
    if b:
        temp.child = b
    return res.child


def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    # pass
    if head is None or head.next is None:
        return head
    temp = head
    temp.next = flattenLinkedList(temp.next)

    res = mergeList(temp,temp.next) 
    return res
