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
