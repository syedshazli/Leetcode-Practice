# Leetcode-Practice
Join me on my leetcode journey. Problems are based off the Grind 75. Will look to do more after interviews. Read more here: https://www.techinterviewhandbook.org/grind75?hours=10&weeks=11

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
[Problem 6]: Best Stock Price: You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

*Notes
* Set the smallest  to the first element
* Loop through, if current stock is less than smallest set current to smallest
* If the next element minus smalelst is greater than a max variable
* Set max variable to next element minus smallest
*  Return max variable
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Problem 7]: Valid Palindrome: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


*Notes
* s.replaceAll("\\p{Punct}", ") will remove punctuations, and .toLowerCase and replaceAll (" ", "") will remove all spaces and convert uppercase to lowercase
* This could honestly be a stack problem, maybe redo as a stack question
* Create a new string and add letters from back to front
* Look very closely for syntax to adding from back to front
* If that string is equal to original, true, if not, false.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[FIRST DYNAMIC PROGRAMMING PROBLEM: Problem 8]: Climbing Stairs: You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

   *Notes
   * This is a Dynamic Programming problem that involves using the Fibonacci sequence. To find the # of ways to get to the nth step you need the n-1 and n-2 step
   * I tried using recursion for fibonacci sequence before but we ran out of time. This is because you are taking up extra time computing steps that you found previously. When things get big to something like n = 45, this becomes a problem. THIS MEANS USE MEMOIZATION
   * Instead I removed the recursion aspect all together and stored everything in an array of size n+1.
   * Set "base cases." arr[0] will be 1, arr[1] is 1, and arr[2] is 2. (arr[0] is 1 in order to make arr[2] = arr[1] + arr[0] true)
   * From i to n, if i is not 0, 1, 2, arr[n] equals arr[n-1] + arr[n-2]
   * Return n.
   * My first Dynamic Programming problem. Was getting out of bounds errors for a bit and had to manipulate size of the array to figure it out
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Problem 9]: Majority Element: Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 *Notes
* I wanted to design this with a hashmap, so I decided we wanted the key to be the actual number in the array
* And the value to be number of times the number was found
* With the getOrDefault method, if the number was already present, we added 1 to the value of the key
* If the key is greater than length of array/2, then we found our number. Return this number as the answer
* If this was never accessed, return 0
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Problem 10]: Contains Duplicate: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false

*Notes
* I immedietley related this to a Hashset problem due to us using similar logic in DFS/BFS
* Use a HashSet of integers
* From i to nums.length, if we've seen the number ( seen.contains(nums[i] ) return true
* Otherwise, add the number to the hash set
* Return false outside the loop
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
