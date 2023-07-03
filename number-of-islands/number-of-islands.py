class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows, numColumns = len(grid), len(grid[0])
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs(row: int, col: int) -> None:
            if (not (0 <= row < numRows) or not (0 <= col < numColumns)):
                return
            elif (grid[row][col] == "0" or (row, col) in visited):
                return
            
            grid[row][col] = "0"
            visited.add((row, col))

            for neigh in neighbours:
                dfs(row + neigh[0], col + neigh[1])
            
            return 


        numIslands = 0
        for row in range(numRows):
            for col in range(numColumns):
                visited.add((row, col))
                if (grid[row][col] == "1"): # Land
                    numIslands += 1

                    for neigh in neighbours:
                        dfs(row + neigh[0], col + neigh[1])

        return numIslands
        