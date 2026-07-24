# _____________________________ BRUTE FORCE APPROACH ___________________________

# from collections import deque
# class Stack:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()
#     def push(self , x):
#         self.q2.append(x)
#         while self.q1:
#             self.q2.append(self.q1.popleft())
#         while self.q2:
#             self.q1.append(self.q2.popleft())
#     def pop(self):
#         return self.q1.popleft()
#     def peek(self):
#         return self.q1[0]
#     def isEmpty(self):
#         return len(self.q1) == 0

# _______________________________ OPTIMAL SOLUTION ________________________

from collections import deque
class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self , x):
        self.q1.append(x)
    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q1 , self.q2 = self.q2 , deque()
        return val
    def peek(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q2.append(val)
        self.q1 , self.q2 = self.q2 , self.q1
        return val
        
    def isEmpty(self):
        return not self.q1

q = Stack()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())
print(q.pop())
print(q.peek())