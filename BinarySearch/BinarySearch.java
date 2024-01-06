class Solution {

    public int search(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;

        while (i <= j) {
            // mid is calculated this way to prevent integer overflow.
            // See: https://blog.research.google/2006/06/extra-extra-read-all-about-it-nearly.html
            int mid = i + (j - i) / 2;

            if (nums[mid] == target) return mid; else if (
                nums[mid] < target
            ) i = mid + 1; else j = mid - 1;
        }

        return -1;
    }
}

// Example 1:

// Input: nums = [-1,0,3,5,9,12], target = 9
// Output: 4
// Explanation: 9 exists in nums and its index is 4
// Example 2:

// Input: nums = [-1,0,3,5,9,12], target = 2
// Output: -1
// Explanation: 2 does not exist in nums so return -1
