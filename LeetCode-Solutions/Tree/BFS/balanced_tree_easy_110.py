# _________________________ BFS ________________________
# Time Complexity: O(n ^ 2) and Space Complexity: O(n)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        q = deque([root])

        while q:
            node = q.popleft()

            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if abs(left_height - right_height) > 1:
                return False

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return True

    def height(self, root):
        if root is None:
            return 0

        q = deque([root])
        height = 0

        while q:
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            height += 1

        return height

# Create tree:
#       3
#      / \
#     9  20
#        / \
#       15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.isBalanced(root))  # Output: True

# _____________________________ DFS ________________________

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)

            if left == -1:
                return -1

            right = dfs(root.right)

            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root)


# Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()

result = solution.isBalanced(root)

if result != -1:
    print("Balanced")
else:
    print("Not Balanced")