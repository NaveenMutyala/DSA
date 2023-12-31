public boolean isValid(String s) {
        if(s.length()%2 !=0)
            return false;
        Stack<Character> stk = new Stack<>();

        for(int i=0;i<s.length();i++){

            if(
                stk.isEmpty() 
                && (s.charAt(i) == ')' || s.charAt(i) == '}' || s.charAt(i) == ']' )
                ) {
                    return false;
                    }
            else{
                if(s.charAt(i)==')' && stk.peek() == '(') stk.pop();
                else if(s.charAt(i)=='}' && stk.peek() == '{') stk.pop();
                else if(s.charAt(i)==']' && stk.peek() == '[') stk.pop();
                else stk.push(s.charAt(i));

            }


        }

        return stk.isEmpty();
    }


// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false
