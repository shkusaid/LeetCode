class Node:
    def __init__(self , val):
        self.val = val
        self.next = None

class List:
    def __init__(self):
        self.head = None
    def adding_node(self ,x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

    def remove_duplicate(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.head
        current = self.head.next
        prev = self.head
        while current:
            if prev.val != current.val:
                prev = current
                current = current.next
            else:
                current = current.next
                prev.next = current
        return self.display()
    

ll = List()
ll.adding_node(1)
ll.adding_node(1)
ll.adding_node(2)
ll.adding_node(2)
ll.adding_node(3)
ll.adding_node(4)
ll.remove_duplicate()