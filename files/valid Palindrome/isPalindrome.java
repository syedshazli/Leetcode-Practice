*Notes
* s.replaceAll("\\p{Punct}", ") will remove punctuations, but .toLowerCase and replaceAll (" ", "") will remove all spaces and convert uppercase to lowercase
* This could honestly be a stack problem, maybe redo as a stack question
* Create a new string and add letters from back to front
* Look very closely for syntax to adding from back to front
* If that string is equal to original, true, if not, false.

class Solution {
    public boolean isPalindrome(String s) {
     String result = s.replaceAll("\\p{Punct}", "");
    String next = result.toLowerCase();
    next = next.replaceAll(" ", "");
   // Stack<String> stack = new Stack<>();
   String test = "";
    for(int i = 0; i<next.length(); i++){
          test += next.substring(next.length()-i-1, next.length()-i);
    }
    
    if(!test.equals(next)){System.out.println(test);return false;}
return true;
    }


}
