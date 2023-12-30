 public int maxArea(int[] height) {
        int mx = -1,l =0, r = height.length-1,area=0;
        while(l<r){
            area = Math.abs(l-r)*Math.min(height[l],height[r]);
            mx= Math.max(mx,area);
            if(height[l]>height[r]){
                r-=1;
            }
            else{
                l+=1;
            }
        }
        return mx;
    }


// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
// Example 2:

// Input: height = [1,1]
// Output: 1
