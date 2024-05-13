/**
*Notes
* This is a notroious stack problem. How do we recognize this?
*  We can notice this by seeing that the answer directly depends on a corresponding element
*  Each time we have a opening parentheses, push the closing parenthesis to the stack
*  If the stack is empty or we don't find the closing parenthesis next, we return false
*  Else, it's true.
*/

class validParentheses {
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<Character>();

        for(char c : s.toCharArray()){

            if(c == '('){
                stack.push(')');
                }

            else if(c == '{') {
                stack.push('}');
                }

            else if(c == '[') {
                stack.push(']');
                }

            else if( stack.isEmpty() ||stack.pop() != c ){
                return false;
                }


        }
        return stack.isEmpty(); //means true if empty because everything matched and we too everything out of the stack     
    }
}
