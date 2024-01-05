public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<Pair<Integer,Integer>> stack = new Stack<>();
        for(int i=0;i<heights.length;i++){
            int start = i;
            int h = heights[i];
            while(!stack.isEmpty() && stack.peek().getValue() > h){
                int index = stack.peek().getKey();
                int height = stack.peek().getValue();
                stack.pop();
                maxArea = Math.max(maxArea, height*(i-index));
                start = index;
            }
            stack.push(new Pair(start,h));
        }

        while (!stack.isEmpty()){
            Pair<Integer,Integer> pair = stack.pop();
            int i = pair.getKey();
            int h = pair.getValue();
            maxArea = Math.max(maxArea,h*(heights.length-i));
        }

        return maxArea;
    }
