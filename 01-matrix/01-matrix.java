import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int numRows = mat.length, numCols = mat[0].length;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        ArrayDeque<int[]> deque = new ArrayDeque<int[]>();
        boolean[][] visited = new boolean[numRows][numCols];
        int[][] result = new int[numRows][numCols];

        // Add 0s to the deque
        for (int row = 0; row < numRows; row++) {
            for (int col = 0; col < numCols; col++) {
                if (mat[row][col] == 0) {
                    deque.addLast(new int[]{row, col});
                    visited[row][col] = true; 
                }
            }
        }

        int distance = 0;
        while (deque.size() > 0) {
            int breadth = deque.size();

            while (breadth > 0) {
                int[] curr = deque.removeFirst();
                int row = curr[0], col = curr[1];

                visited[row][col] = true; 
                result[row][col] = distance; 
                
                // Add neighbours to deque
                for (int[] dir : directions) {
                    int nRow = row + dir[0], nCol = col + dir[1];
                    boolean isValid = (0 <= nRow) && (nRow < numRows) && (0 <= nCol) && (nCol < numCols);

                    if (isValid && !visited[nRow][nCol]) {
                        deque.addLast(new int[]{nRow, nCol});
                        visited[nRow][nCol] = true; 

                    }
                }
                breadth -= 1;
            }
            distance += 1;
        }

        return result; 
    }
}