# ________________________ BFS ________________________

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])

        while q:
            size = len(q)
            total = 0

            for _ in range(size):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(total / size)

        return ans


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
print(solution.averageOfLevels(root))


# ______________________________ DFS ________________________

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = []
        counts = []

        def dfs(node, level):
            if not node:
                return

            if level == len(sums):
                sums.append(0)
                counts.append(0)

            sums[level] += node.val
            counts[level] += 1

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        ans = []

        for i in range(len(sums)):
            ans.append(sums[i] / counts[i])

        return ans


# Tree:
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
print(solution.averageOfLevels(root))