public int[] twoSum(int[] nums, int target) 
    {
        int arr[] = new int[2];
        int i=0,j=nums.length-1;
        while(i<j){
            if(nums[i]+nums[j] > target){
                while(nums[j-1]==nums[j])j--;
                j--;
            }
            else if ((nums[i]+nums[j])<target){
                while(nums[i+1]==nums[i])i++;
                i++;
            }
            else{
                arr[0]=i+1;
                arr[1]=j+1;
                break;
            }
        }
        return arr;
        
    }


// Example 1:

// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
// Example 2:

// Input: numbers = [2,3,4], target = 6
// Output: [1,3]
// Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
// Example 3:

// Input: numbers = [-1,0], target = -1
// Output: [1,2]
// Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 
