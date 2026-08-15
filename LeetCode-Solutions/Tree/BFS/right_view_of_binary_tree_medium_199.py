# ____________________ BFS ____________________

from collections import deque
from logging import root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def right_view(self, root):
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size -1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# sol = Solution()
# print(sol.right_view(root))  # Output: [1, 3, 7]


# ____________________ DFS ____________________
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        ans = []

        def dfs(node, depth):
            if node is None:
                return

            if depth == len(ans):
                ans.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return ans


# Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

# Call function
sol = Solution()
print(sol.rightSideView(root))
