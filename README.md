# Leetcode-Practice
Join me on my leetcode journey.

Notes for specific problems:

[Problem 1]: Invert Binary Tree: Given the root of a binary tree, invert the tree, and return its root.

*Notes on Problem
* My implementation is a Post Order Traversal of the Tree
* The implementation uses recursion to find the leaf nodes, which then return the parent node to allow swapping
* Set the value of the left and right nodes to new TreeNode variables
* We switch the left and the right of the roots to ivnert the tree properly
* 
![image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/7b5327f3-bec2-45f7-bbdf-9a9c6b2041ad)






------------------------------------------------------------------------------------------------------------------------------------------------

[Problem 2]: Binary Search: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

*Notes on Problem

* Think of the search like an array where you split the size each time you finish iterating the while loop
* Look closely at how we determine the middle of the array. It is low + ((high -low)/2) You initially thought that low was included in the parenthesis
* We set val to the middle value to determine if our target is higher or lower than our middle value
* If the target is higher, then we need to increase the lower bound of the array by middle+1
* If the target is lower than the middle, we need to decrease the upper bound of the array by middle-1
* If it's neither, we are at the target! Return the index.

------------------------------------------------------------------------------------------------------------------------------------------------
[Problem 3]: Two sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

*Notes on Problem
*This solution is O(n^2). When you redo, can you think of a better solution using hashmap? Maybe store target in a hashmap?
*Double for loop that returns the indexes the two numbers in a array that add up to target
* i!=j ensures we are not adding up the same element
 
------------------------------------------------------------------------------------------------------------------------------------------------
[Problem 4]: firstBadVersion: You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

 *Notes    
   * This is a binary search problem as we want to minimize function calls, so instead of O(n) with binary search it is O( log n)
      * Everything about the binary search stays the same. However, to minimize isBadVersion calls, if we're at a bad version in the middle, we make our upper bound the middle.
      * our answer will reside in our variable low. This is because we keep decreasing high if it's a bad version, and increasing low if not. At the point where low>high, we found the bad version
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Problem 5]: Valid Parentheses: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

*Notes
* This is a notroious stack problem. How do we recognize this?
*  We can notice this by seeing that the answer directly depends on a corresponding element
*  Each time we have a opening parentheses, push the closing parenthesis to the stack
*  If the stack is empty or we don't find the closing parenthesis next, we return false
*  Else, it's true.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
