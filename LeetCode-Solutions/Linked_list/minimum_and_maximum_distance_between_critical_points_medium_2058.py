from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        index = 1
        positions = []

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                positions.append(index)

            prev = curr
            curr = curr.next
            index += 1

        if len(positions) < 2:
            return [-1, -1]

        minimum = float('inf')

        for i in range(1, len(positions)):
            minimum = min(
                minimum,
                positions[i] - positions[i - 1]
            )

        maximum = positions[-1] - positions[0]

        return [minimum, maximum]

values = [5, 3, 1, 2, 5, 1, 2]

head = ListNode(values[0])
current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


# Run solution
solution = Solution()
result = solution.nodesBetweenCriticalPoints(head)

print("Input:", values)
print("Output:", result)