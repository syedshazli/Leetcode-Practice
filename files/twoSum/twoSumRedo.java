/**
*Notes
* Optimized solution this time, O(n) instead of O(n^2)
* create a hashmap
* loop through array, constantly updating a variable equal to "target - nums[i]" after every iteration
* if the variable created is present in the hashmap
*     set the start index to the map.get(variable)
*     set the second index to the current index
*          break to reduce runtime
* Outside of the if, add the current value and its index to map
* (added at the end to avoid self reference)

*/


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
        break; //reached our goal
          }

map.put( nums[i] , i );//added at the end to avoid self reference
    } //end for loop
    
   return correct;
    }
  
    
    }
