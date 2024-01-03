public int carFleet(int target, int[] position, int[] speed) {
        Stack<Double> stk = new Stack<>();
        if (position.length ==1) return 1;
        int combine[][] = new int[position.length][2];
        for(int i =0;i<position.length;i++){
            combine[i][0] = position[i];
            combine[i][1] = speed[i];
        }
        Arrays.sort(combine,java.util.Comparator.comparingInt(o -> o[0]));
        for(int i=position.length-1;i>=0;i--){
            double currTime =(double) (target-combine[i][0])/combine[i][1];
            if(!stk.isEmpty() && currTime<=stk.peek()){
                continue;
            }else{
                stk.push(currTime);
            }
        }
        return stk.size();
    }

// Example 1:

// Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
// Output: 3
// Explanation:
// The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
// The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
// The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
// Note that no other cars meet these fleets before the destination, so the answer is 3.
// Example 2:

// Input: target = 10, position = [3], speed = [3]
// Output: 1
// Explanation: There is only one car, hence there is only one fleet.
// Example 3:

// Input: target = 100, position = [0,2,4], speed = [4,2,1]
// Output: 1
// Explanation:
// The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
// Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
