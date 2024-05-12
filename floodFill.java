/**
*Notes
* First DFS implementation, congrats!
* A relativley easy problem once you understand what 4 directional means
* This means anywhere up, down, left, right connected to our image[sr][sc]
* We can only alter values that have the same value as the original image[sr][sc] and are related some way (either distantly or direct) 4 directionally 
* We need to create a DFS helper function as a result
* First update the current color to the target. Then find if any left, right, up, down equal the oldTarget, and if so call dfs with these parameters
* left means row-1, right means row+1, up means col-1, down means col+1. Make sure the bounds are valid as well
* IMPORTANT: base case in main function is that if the image[sr][sc] equals target then we return image
* My solution is DFS because once we find a valid 4 directional spot, we suspend all operations and explore this spot further and try to find its neighbors
*
*/

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
            if(image[sr][sc] == color ){return image;}

            int oldTarget = image[sr][sc];
           
            dfs(oldTarget, color, sr, sc, image); //perform DFS! Congratulations on your first DFS implementation!

            return image;
    }

    public static void dfs(int oldTarget, int newTarget, int sr, int sc, int[][] image){
        //Happy exploring!
        
        //try to find left, right, up, down (4 directionally) with same val as oldTarget
        //update the val to newTarget

        int rowLength = image.length;
        int columnLength = image[0].length;

        //change the current color with the target
        image[sr][sc] = newTarget;

        //conditions for left, right, up, down if they match the oldTarget
        if(sr-1>=0 && (image[sr-1][sc] == oldTarget) ){dfs(oldTarget, newTarget, sr-1, sc, image);}
        if(sr+1<rowLength && (image[sr+1][sc] == oldTarget) ){dfs(oldTarget, newTarget, sr+1, sc, image);}
        if(sc-1>=0 && (image[sr][sc-1] == oldTarget) ){dfs(oldTarget, newTarget, sr, sc-1, image);}
        if(sc+1<columnLength && (image[sr][sc+1] == oldTarget) ){dfs(oldTarget, newTarget, sr, sc+1, image);}


        
        


    }


}
