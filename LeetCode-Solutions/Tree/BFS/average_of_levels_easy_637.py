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