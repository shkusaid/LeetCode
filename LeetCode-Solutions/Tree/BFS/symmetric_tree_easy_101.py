from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        q = deque([p , q]) # if have two tree 
        # q = deque([root.left , root.right]) # if have one tree
        while q:
            n1 = q.popleft()
            n2 = q.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)
        return True

p1 = TreeNode(1)
p1.left = TreeNode(3)
p1.right = TreeNode(2)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

sol = Solution()
print(f"Test Case 1: {sol.isSameTree(p1, q1)}")  # Output: True