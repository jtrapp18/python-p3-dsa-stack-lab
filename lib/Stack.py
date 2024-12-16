class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            print("error")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        
        search_items = self.items.copy()

        i = 0
        while search_items:
            curr_search = search_items.pop()
            if curr_search == target:
                return i
            else:
                i += 1
            
        return -1

# stk = Stack()
# print("isEmpty", stk.isEmpty())
# print("size", stk.size() == 0)
# print("pop", stk.pop() == None)
# stk.push(1)
# print("is not Empty", not stk.isEmpty())
# print("size", stk.size() == 1)
# print("pop", stk.pop() == 1)

# stk = Stack([1], 1)

# print(stk.full())
# print(stk.size() == 1)
# print(stk.pop() == 1)
# stk.push(1)
# stk.push(2)