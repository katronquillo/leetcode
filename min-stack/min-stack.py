class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = None

    def push(self, val: int) -> None:
        if ((self.minElement is None) or (self.minElement and self.minElement > val)):
            self.minElement = val
        
        newValue = (val, self.minElement)
        self.stack.append(newValue)
        
    def pop(self) -> None:
        self.stack.pop()

        if (len(self.stack) == 0):
            self.minElement = None
        else:
            _, currMin = self.stack[-1]
            if self.minElement != currMin:
                self.minElement = currMin 

    def top(self) -> int:
        topVal, _ = self.stack[-1]
        return topVal

    def getMin(self) -> int:
        return 0 if (self.minElement is None) else self.minElement 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()