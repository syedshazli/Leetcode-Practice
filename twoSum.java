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
