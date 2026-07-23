# _______________________ BRUTE FORCE APPROACH _____________________

# class Stack:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#     def push(self , val):
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())
#         self.stack1.append(val)
#         while self.stack2:
#             self.stack1.append(self.stack2.pop())
#     def pop(self):
#         return self.stack1.pop(0)
#     def peek(self):
#         return self.stack1[0]
#     def is_empty(self):
#         return len(self.stack1) == 0

# _________________________ OPTIMAL APPROACH _______________________

class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self , val):
        self.stack1.append(val)
    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def peek(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.peek())
st.pop()
print(st.peek())

