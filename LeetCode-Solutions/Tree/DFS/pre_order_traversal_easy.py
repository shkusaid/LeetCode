class Tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)


tree = Binary_tree()

tree.root = Tree_node(1)
tree.root.left = Tree_node(2)
tree.root.right = Tree_node(3)

tree.root.left.left = Tree_node(4)
tree.root.left.right = Tree_node(5)

tree.pre_order_traversal(tree.root)