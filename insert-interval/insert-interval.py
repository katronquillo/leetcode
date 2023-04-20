class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd, inserted = newInterval[0], newInterval[1], False
        result = []

        for i in range(len(intervals)):
            currInterval = intervals[i]
            currStart, currEnd = currInterval[0], currInterval[1]

            # Starts after new interval - Insertion Point
            if (currStart > newEnd):
                result.append([newStart, newEnd])
                result += intervals[i:]
                inserted = True
                break
            else:
                # Possible overlap - May need to merge intervals
                newOverlapCurr = newStart >= currStart and newStart <= currEnd
                currOverlapNew = currStart >= newStart and currStart <= newEnd
                if (newOverlapCurr or currOverlapNew):
                    newStart = min(newStart, currStart)
                    newEnd = max(newEnd, currEnd)
                else:
                    result.append(currInterval)
        
        if (not inserted):
            result.append([newStart, newEnd])
                    
        return result