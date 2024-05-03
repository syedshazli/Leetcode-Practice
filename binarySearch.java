/**
*Must retry problem later
*Notes on Problem
* Think of the search like an array where you split the size each time you finish iterating the while loop
* Look closely at how we determine the middle of the array. It is low + ((high -low)/2) You initially thought that low was included in the parenthesis
* We set val to the middle value to determine if our target is higher or lower than our middle value
* If the target is higher, then we need to increase the lower bound of the array by middle+1
* If the target is lower than the middle, we need to decrease the upper bound of the array by middle-1
* If it's neither, we are at the target! Return the index.
*/

public class binarySearch {
    int[]nums = {2, 3, 4, 5};
    System.out.println("Binary search returned "+search(nums, 4));

    public int search(int[] nums, int target) {
        
        int low = 0;
        int high = nums.length-1;

        while(low<= high){
            int middle = low+(high-low)/2;
            int val = nums[middle];


        

       if(val>target){ //middle number exceeded target value, decrease upper bound

            high = middle-1;
        }

        else if(val<target){//middle number was too low, increase the bound
            low = middle +1;
        }
        else{return middle;}

        }

       

       

        return -1;

    }
}
