/**
*This solution is O(n^2). When you redo, can you think of a better solution using hashmap? Maybe store target in a hashmap?
*Double for loop that returns the indexes the two numbers in a array that add up to target
* i!=j ensures we are not adding up the same element
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
         int[] correct = new int[2];
        
    for(int i = 0; i< nums.length; i++){
        for(int j = 1; j<nums.length; j++){
            if(nums[i] + nums[j] == target && i!= j){correct[0] = i; correct[1] = j;}
        }
    }
           
return correct;
        }
           // throw new IllegalArgumentException("NO match found");
    }
