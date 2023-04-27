class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList();

        for (int index = 0; index < nums.length; index++) {
            // Ignore duplicate integers
            if (index > 0 && nums[index] == nums[index - 1]) {
                continue;
            }
            else {
                int i = nums[index];
                int left = index + 1, right = nums.length - 1;
                int target = 0 - i;

                while (left < right && left < nums.length && right >= 0) {
                    int j = nums[left], k = nums[right];
                    if (j + k < target) {
                        left += 1;
                    }
                    else if (j + k > target) {
                        right -= 1;
                    }
                    else {
                        result.add(Arrays.asList(i, j, k));
                        left += 1;
                        right -= 1;

                        while (left < right && nums[left] == nums[left - 1]) {
                            left += 1;
                        }

                        while (left < right && nums[right] == nums[right + 1]) {
                            right -= 1;
                        }
                    }
                }
            }
        }

        return result;
    }
}