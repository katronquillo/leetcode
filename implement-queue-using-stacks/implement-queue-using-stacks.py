from collections import deque
class MyQueue:

    def __init__(self):
        self.pushStack = deque()
        self.popStack = deque()
        
    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        self._move()
        return self.popStack.pop()
        
    def peek(self) -> int:
        self._move()
        topItem = self.popStack.pop()
        self.popStack.append(topItem)
        return topItem

    def _move(self) -> None:
        if (len(self.popStack) == 0 and len(self.pushStack) > 0):
            while (len(self.pushStack) > 0):
                self.popStack.append(self.pushStack.pop())    

    def empty(self) -> bool:
        return len(self.pushStack) == 0 and len(self.popStack) == 0
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()