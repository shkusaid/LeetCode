# __________________________ USING DFS __________________________

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def levelOrder(self, root):
#         ans = []

#         def dfs(root, level):
#             if root is None:
#                 return

#             if level == len(ans):
#                 ans.append([])

#             ans[level].append(root.val)

#             dfs(root.left, level + 1)
#             dfs(root.right, level + 1)

#         dfs(root, 0)
#         return ans


# root = TreeNode(
#     3,
#     TreeNode(9),
#     TreeNode(
#         20,
#         TreeNode(15),
#         TreeNode(7)
#     )
# )

# print(Solution().levelOrder(root))

# ___________________________ USING BFS __________________________
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans


# Create tree
root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)

# Test
solution = Solution()
print(solution.levelOrder(root))