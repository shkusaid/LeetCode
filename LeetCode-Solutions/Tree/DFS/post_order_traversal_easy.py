class Tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self):
        self.root = None

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=' ')


tree = Binary_tree()

tree.root = Tree_node(1)
tree.root.left = Tree_node(2)
tree.root.right = Tree_node(3)

tree.root.left.left = Tree_node(4)
tree.root.left.right = Tree_node(5)

tree.post_order_traversal(tree.root)