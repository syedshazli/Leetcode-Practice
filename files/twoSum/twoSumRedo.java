class Solution {
    public int[] twoSum(int[] nums, int target) {
        
         int[] correct = new int[2];
   

//HashMap to store the number as the key and the index as the value.

// for loop over numslist

// return  newarray [index, index2]
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

int sumVal = 0;


for(int i = 0; i<nums.length; i++){

sumVal = target- nums[i];


    if(map.containsKey(sumVal)){
        correct[0] = map.get(sumVal);
        correct[1] = i; 
          }

map.put( nums[i] , i );//added at the end to avoid self reference
    } //end for loop
    
   return correct;
    }
  
    
    }
