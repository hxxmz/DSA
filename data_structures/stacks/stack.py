
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
        return self.size()
    
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)

if __name__ == "__main__":
    stk = Stack()
    print(stk.push(10))
    print(stk.peek())
    print(stk.push(5))
    stk.display()
    print(stk.peek())
    print(stk.pop())
    print(stk.peek())
    print(stk.size())
    stk.display()
