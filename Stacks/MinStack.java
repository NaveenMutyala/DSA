class MinStack {

    Stack<Integer> stk,minStk;
    public MinStack() {
       stk = new Stack<>();
       minStk = new Stack<>();
    }
    
    public void push(int val) {
        stk.push(val);
        val = Math.min(val, minStk.isEmpty()?val: minStk.peek());
        minStk.push(val);
        
    }
    
    public void pop() {
        stk.pop();
        minStk.pop();
    }
    
    public int top() {
       return stk.peek();
    }
    
    public int getMin() {
       return minStk.peek();
    }
}


