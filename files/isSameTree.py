# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We want to make sure we can check if the left nodes exist for both, and if they do, are they the same value. The same thing can be said for the right nodes. If at our base case, one is none and the other isn't return false. Otherwise return true 

# Approach
Our base cases cover the situation where both nodes are none, or one contains a value and the other doesn't. So then once these are returned, if just one of the cases in the return comes up as False (such as values not being equal), the function returns false as well. So after the base cases, return the recursive solution for right, left and if val's are equal
