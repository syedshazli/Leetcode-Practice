/**
*Review and try to complete w/a hashmap
*will retry in a couple days
*/

class Solution {
    public int maxProfit(int[] prices) {
        // find the greatest difference in sorted form
        // index matters, earlier the index the earlier the day

        // if you buy something early and can sell it later
        // the max is the difference between the two
        // brute force method

        
        int largest = prices[0];
      
        int max = 0;
        for (int i = 1; i < prices.length; i++) {
          
            if(prices[i]<largest){
                largest = prices[i];


                //max = prices[i];



                }

           else if(prices[i]- largest> max){
            max = prices[i] - largest;
           }

            }

           return max;  // do something
        }
       
    }
