class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        a, b = a[::-1], b[::-1]

        carryOver = 0
        for i in range(max(len(a), len(b))):
            aDigit = int(a[i]) if (i < len(a)) else 0
            bDigit = int(b[i]) if (i < len(b)) else 0
            
            colSum = aDigit + bDigit + carryOver
            carryOver = colSum // 2
            char = str(colSum % 2)
            result = char + result
        
        if (carryOver == 1):
            result = "1" + result
        
        return result 
            
