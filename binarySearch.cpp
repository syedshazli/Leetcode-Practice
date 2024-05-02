class binarySearch {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size()-1;

        while(high>= low){
            int middle = low+(high-low)/2;
            int val = nums[middle];
            if(val>target){
                    high= middle-1;
            }
            else if(val<target){ //our target is bigger than middle value

            low = middle +1;
            }

            else{return middle;}//we want to return the index, not value of target, which is why we return middle
        }
        return -1;


    }
};
