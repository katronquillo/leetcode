from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue, visited = deque(), set()

        # Add initial rotten oranges to queue + Get number of initial fresh oranges
        numFreshOranges = 0
        for row in range(numRows):
            for col in range(numCols):
                if (grid[row][col] == 1):
                    numFreshOranges += 1
                elif (grid[row][col] == 2):
                    queue.append((row, col))
        
        numMinutes = 0
        while (len(queue) > 0 and numFreshOranges > 0):
            numRottenOranges = len(queue)
            for _ in range(numRottenOranges):
                currRow, currCol = queue.popleft()
                
                if ((currRow, currCol) in visited):
                    continue
                else:
                    visited.add((currRow, currCol))

                    # Fresh orange becomes rotten
                    if (numMinutes > 0):
                        grid[currRow][currCol] = 2
                        numFreshOranges -= 1
                    
                    # Visit neighbours of rotten oranges
                    for n in neighbours:
                        nRow, nCol = currRow + n[0], currCol + n[1]
                        isValid = (0 <= nRow < numRows) and (0 <= nCol < numCols)
                        notVisited = (nRow, nCol) not in visited
                        if (isValid and notVisited and grid[nRow][nCol] == 1):
                            queue.append((nRow, nCol))

            if (len(queue) > 0 and numFreshOranges > 0):
                numMinutes += 1

        return numMinutes if (numFreshOranges == 0) else -1