from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        numRows, numColumns = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = [([0] * numColumns) for _ in range(numRows)]
        queue = deque()
        visited = set()

        # Add Os to the queue 
        for row in range(numRows):
            for col in range(numColumns):
                if (mat[row][col] == 0):
                    queue.append((row, col))
                    visited.add((row, col))

        distance = 0 
        while (len(queue) > 0):
            for _ in range(len(queue)):
                row, col = queue.popleft()

                result[row][col] = distance

                if (result[row][col] == "1"):
                    minDistance = min(distance, minDistance)

                for d in directions:
                    nRow, nCol = row + d[0], col + d[1]

                    isValid = (0 <= nRow < numRows) and (0 <= nCol < numColumns)
                    if (isValid and (nRow, nCol) not in visited):
                        queue.append((nRow, nCol))
                        visited.add((nRow, nCol))

            distance += 1

        return (result)


            

