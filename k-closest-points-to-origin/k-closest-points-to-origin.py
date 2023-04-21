from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points: 
            x, y = point[0], point[1]
            distance = sqrt((x ** 2) + (y ** 2))
            minHeap.append((distance, x, y))
        heapify(minHeap)

        result = []
        for _ in range(k):
            (distance, x, y) = heappop(minHeap)
            result.append([x, y])
        
        return result 