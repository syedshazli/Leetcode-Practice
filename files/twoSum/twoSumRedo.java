class Solution {
    public int[] twoSum(int[] nums, int target) {
        
         int[] correct = new int[2];
   

//HashMap to store the number as the key and the index as the value.

// for loop over numslist

// return  newarray [index, index2]
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
int index = 0;
int sumVal = 0;
int index2 = 0;

for(int i = 0; i<nums.length; i++){

    
   

sumVal = target- nums[i];


    if(map.containsKey(sumVal)){
        index = map.get(sumVal);
        index2 = i;  
          }

map.put( nums[i] , i );
    } //end for loop
     correct[0] = index;
    correct[1] = index2;
   return correct;
    }
  
    
    }
