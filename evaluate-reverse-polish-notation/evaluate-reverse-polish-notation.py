from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = deque()
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                rightOperand = int(stack.pop())
                leftOperand = int(stack.pop())

                if (token == "+"):
                    result = leftOperand + rightOperand
                elif (token == "-"):
                    result = leftOperand - rightOperand
                elif (token == "*"):
                    result = leftOperand * rightOperand
                else:
                    result = leftOperand / rightOperand 
                    result = floor(result) if result >= 0 else ceil(result)
                
                stack.append(result)
        
        result = stack.pop()
        return result 
            
