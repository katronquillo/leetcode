class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] result = new int[k][2];
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(
            (p1, p2) -> getEuclideanDistance(p1).compareTo(getEuclideanDistance(p2))
        );

        // Calculate distance from origin for each point + Add to Priority Queue
        // PQ orders points by ascending distance
        for (int[] point : points) {
            pq.add(point);
        }

        // Add K closest points to origin to result
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll();
        }

        return result;
    }

    public Double getEuclideanDistance(int[] point) {
        return Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
    }
}