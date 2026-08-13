from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        q = deque([p , q])
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
            q.append(n2.left)
            q.append(n1.right)
            q.append(n2.right)
        return True



# -------------------------
# Test Case 1
# -------------------------

# Tree 1:
#       1
#      / \
#     2   3

p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

# Tree 2:
#       1
#      / \
#     2   3

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)


# -------------------------
# Test Case 2
# -------------------------

# Tree 1:
#       1
#      /
#     2

p2 = TreeNode(1)
p2.left = TreeNode(2)

# Tree 2:
#       1
#        \
#         2

q2 = TreeNode(1)
q2.right = TreeNode(2)


# -------------------------
# Test Case 3
# -------------------------

# Tree 1:
#       1
#      / \
#     2   1

p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)

# Tree 2:
#       1
#      / \
#     1   2

q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)


# -------------------------
# Run tests
# -------------------------

solution = Solution()

print("Test Case 1:", solution.isSameTree(p1, q1))
print("Test Case 2:", solution.isSameTree(p2, q2))
print("Test Case 3:", solution.isSameTree(p3, q3))