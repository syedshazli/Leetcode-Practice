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
