/**
*Notes
   * This is a Dynamic Programming problem that involves using the Fibonacci sequence. To find the # of ways to get to the nth step you need the n-1 and n-2 step
   * I tried using recursion for fibonacci sequence before but we ran out of time. This is because you are taking up extra time computing steps that you found previously. When things get big to something like n = 45, this becomes a problem. THIS MEANS USE MEMOIZATION
   * Instead I removed the recursion aspect all together and stored everything in an array of size n+1.
   * Set "base cases." arr[0] will be 1, arr[1] is 1, and arr[2] is 2. (arr[0] is 1 in order to make arr[2] = arr[1] + arr[0] true)
   * From i to n, if i is not 0, 1, 2, arr[n] equals arr[n-1] + arr[n-2]
   * Return n.
     */
class Solution {
    public int climbStairs(int n) {

        int[] arr = new int [n+1];

        for(int i = 0; i<=n; i++){
              if (i <=2){arr[i] = i; arr[0] = 1; }
            
            
            
            else{
                System.out.print(arr[i]);
                arr[i] = arr[i-1] + arr[i-2];
            }

        }

return arr[n];

