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

    def sort_linked_list(self):
        dummy0 = Node(0)
        dummy1 = Node(0)
        dummy2 = Node(0)
        head0 = dummy0
        head1 = dummy1
        head2 = dummy2
        temp = self.head
        while temp:
            if temp.val == 0:
                head0.next = temp
                head0 = head0.next
            elif temp.val == 1:
                head1.next = temp
                head1 = head1.next
            else:
                head2.next = temp
                head2 = head2.next
            temp = temp.next
        head0.next = dummy1.next
        head1.next = dummy2.next
        head2.next = None
        self.head = dummy0.next
        return self.display()

ll = List()
ll.adding_node(1)
ll.adding_node(2)
ll.adding_node(0)
ll.adding_node(1)
ll.adding_node(2)
ll.adding_node(0)
ll.adding_node(0)
ll.sort_linked_list()