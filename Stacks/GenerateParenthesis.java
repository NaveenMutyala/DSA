Stack<Character> stack = new Stack<>();
        List<String> res = new ArrayList<>();
    public List<String> generateParenthesis(int n) {

    

         

        this.backtrack(0, 0, n);
        return res;
    

    }

    public void backtrack(int openN, int closedN, int n) {
            if (openN == closedN && closedN == n) {
                Iterator vale = this.stack.iterator();
                String temp = "";
                while (vale.hasNext()) {
                    temp = temp + vale.next();
                }
                res.add(temp);
            }
            if (openN < n) {
                stack.push('(');
                backtrack(openN + 1, closedN, n);
                stack.pop();
            }
            if (closedN < openN) {
                stack.push(')');
                backtrack(openN, closedN + 1, n);
                stack.pop();
            }
        }


// Input
// n =
// 3
// Output
// ["((()))","(()())","(())()","()(())","()()()"]
