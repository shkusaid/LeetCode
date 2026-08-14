# _________________________ BFS _________________________

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root is None:
            return ans

        q = deque([root])
        reverse = False

        while q:
            size = len(q)
            level = deque()

            for i in range(size):
                node = q.popleft()

                if reverse:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(list(level))
            reverse = not reverse

        return ans


# Create test tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# Run
solution = Solution()
result = solution.zigzagLevelOrder(root)

print(result)