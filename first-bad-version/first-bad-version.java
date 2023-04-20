/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        int firstBad = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2 ;

            // Current version is good - first bad comes after
            if (!isBadVersion(mid)) {
                left = mid + 1;
            }
            else {
                // Current version is first bad version
                if (mid == 1 || (mid > 1 && !isBadVersion(mid - 1))) {
                    firstBad = mid;
                    return firstBad;
                }   

                // Current version is bad - first bad comes before
                else {
                    right = mid - 1;
                }
            }
        }

        return firstBad;
    }
}