from d_linked_list.node import Node

"""
Empty List: 
    
    None <- Head = Dummy = Tail -> None

One item: 

    None <- Head=Dummy <-> First=Tail <-> Null

Filled List:
    
    None <- Head|Dummy <-> First Node <-> ... <-> Nth=Tail -> None 

"""


class DoubleLinkedList:
    def __init__(self) -> None:
        self.count = 0

        self.head = self.tail = Node()

    def append(self, object_):
        if self.head is self.tail:
            newNode = Node(value=object_, prev=self.head, next=None)
            self.head.next = newNode
            self.tail = newNode
            self.count += 1
            return

        if self.head is not self.tail:
            # add at the end, just before tail
            newNode = Node(value=object_, prev=self.tail, next=None)
            self.tail.next = newNode
            self.tail = newNode
            self.count += 1

    def __str__(self) -> str:
        str_to_ret = []

        cNode: Node = self.head.next

        while cNode != None:
            str_to_ret.append(str(cNode))
            cNode = cNode.next

        return f'<DLList list: [{", ".join(str_to_ret)}]>'
