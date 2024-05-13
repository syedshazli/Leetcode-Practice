/**
*Notes
* I wanted to design this with a hashmap, so I decided we wanted the key to be the actual number in the array
* And the value to be number of times the number was found
* With the getOrDefault method, if the number was already present, we added 1 to the value of the key
* If the key is greater than length of array/2, then we found our number. Return this number as the answer
* If this was never accessed, return 0
*/


class Solution {
    public int majorityElement(int[] nums) {
        int find = nums.length/2;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 0; i<nums.length; i++){
            
            map.put(nums[i], map.getOrDefault(nums[i], 0) +1  ); //we want the value to be number of times it occured

            if (map.get(nums[i]) > find){
            
                return nums[i];
            }
            
        }

return 0;
    }

}
