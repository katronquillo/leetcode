class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int newStart = newInterval[0], newEnd = newInterval[1];
        boolean inserted = false; 
        ArrayList<int[]> result = new ArrayList<int[]>();

        for (int i = 0; i < intervals.length; i++) {
            int[] curr = intervals[i];
            int currStart = curr[0], currEnd = curr[1];

            // At or After Insertion Point - Current interval starts after new interval
            if (currStart > newEnd) {
                if (!inserted) {
                    result.add(newInterval);
                    inserted = true;
                }
                result.add(intervals[i]);
                continue;
            }
            else {
                // Current interval occurs before insertion or overlaps with new interval
                boolean newOverlapsCurr = (newStart >= currStart) && (newStart <= currEnd);
                boolean currOverlapsNew = (currStart >= newStart) && (currStart <= newEnd);
                if (newOverlapsCurr || currOverlapsNew) {
                    newStart = Math.min(newStart, currStart);
                    newEnd = Math.max(newEnd, currEnd);

                    newInterval[0] = newStart;
                    newInterval[1] = newEnd;
                }
                else {
                    result.add(intervals[i]);
                }
            }
        }

        if (!inserted) {
            result.add(newInterval);
        }

        return result.toArray(new int[result.size()][]);
    }
}