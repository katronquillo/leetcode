class Solution:
    """
    Algorithm...
    1. Keep track of the source pixel's original colour
    2. Change the colour of the source pixel
    3. Using DFS, Flood-fill any adjacent pixels that matched the source's original colour
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        numRows, numColumns = len(image), len(image[0])
        originalColor = image[sr][sc]
        visited = set()

        def dfs(row, col):
            if ((row >= numRows or row < 0) or (col >= numColumns or col < 0)):
                return
            elif (image[row][col] != originalColor):
                return
            elif ((row, col) in visited):
                return 
            
            visited.add((row, col))
            image[row][col] = color

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        dfs(sr, sc)
        return image
            
"""

"""

        

