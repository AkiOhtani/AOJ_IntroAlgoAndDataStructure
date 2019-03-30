class Stack:
    data_list = []
    def push(self, a):
        self.data_list.append(a)
    def pop(self):
        return self.data_list.pop()

data = input()
lines = data.strip().split()
stack = Stack()
for line in lines:
    if line == '+':
        num = int(stack.pop()) + int(stack.pop())
        stack.push(num)
    elif line == '-':
        num = int(stack.pop()) - int(stack.pop())
        stack.push(-1*num)
    elif line == '*':
        num = int(stack.pop()) * int(stack.pop())
        stack.push(num)
    else:
        stack.push(line)

print(stack.pop())