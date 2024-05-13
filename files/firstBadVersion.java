/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); 
      *Notes
      * This is a binary search problem as we want to minimize function calls, so instead of O(n) with binary search it is O( log n)
      * Everything about the binary search stays the same. However, to minimize isBadVersion calls, if we're at a bad version in the middle, we make our upper bound the middle.
      * our answer will reside in our variable low. This is because we keep decreasing high if it's a bad version, and increasing low if not. At the point where low>high, we found the bad version
      
      */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int high = n;
        int low = 1;
        int check = 0;
        while(high >= low){
            int middle = low + (high-low)/2;

            if(isBadVersion(middle)){
                high = middle-1;
            }

            else{low = middle+1;}
            //sample size is too good, let's increase lower bound

             

          
 check = low;
        }
       
 return check;
    }
}
