class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        numRows, numCols = len(matrix), len(matrix[0])
        directionOrder = ["right", "down", "left", "up"]
        directions = {
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
            "up": (-1, 0)
        }

        currRow, currCol, currDirectionIndex = 0, 0, 0
        cLeft, cRight, rTop, rBottom = 0, numCols - 1, 0, numRows - 1
        while (cLeft <= cRight and rTop <= rBottom):
            result.append(matrix[currRow][currCol])

            nextRow = directions[directionOrder[currDirectionIndex % 4]][0] + currRow
            nextCol = directions[directionOrder[currDirectionIndex % 4]][1] + currCol

            # Change the direction if upcoming is out of bounds
            if (nextCol > cRight):
                currDirectionIndex += 1
                rTop += 1
            elif (nextRow > rBottom):
                currDirectionIndex += 1
                cRight -= 1
            elif (nextCol < cLeft):
                currDirectionIndex += 1
                rBottom -= 1
            elif (nextRow < rTop):
                currDirectionIndex += 1
                cLeft += 1
            
            currRow += directions[directionOrder[currDirectionIndex % 4]][0]
            currCol += directions[directionOrder[currDirectionIndex % 4]][1]

        return result