from collections import deque
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
def top_view(root):
    if not root:
        return []
    q = deque([(root , 0)])
    tree_map = {}
    while q:
        node , v = q.popleft()
        if v not in tree_map:
            tree_map[v] = node.val
        if node.left:
            q.append((node.left , v - 1))
        if node.right:
            q.append((node.right , v + 1))
    return [tree_map[v] for v in sorted(tree_map)]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Top View:", top_view(root)) # Top View: [4, 2, 1, 3, 6]