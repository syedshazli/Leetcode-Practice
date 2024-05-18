# Leetcode-Practice
Join me on my leetcode journey. Problems are based off the Neetcode 150. Will look to do more after interviews. Read more here: https://www.techinterviewhandbook.org/grind75?hours=10&weeks=11
.                               Additionally, to enhance my Python skills, I will be completing tasks on CodeWars. Read more about CodeWars here: https://www.codewars.com/kata/515e271a311df0350d00000f/train/python 
* Side note: I will be on vacation from May 16th-June 1. Can't gurantee that I will be able to commit every day but I am definitley going to do a lot to prepare.

Notes for specific problems:

EASY: [Problem 1]: Invert Binary Tree: Given the root of a binary tree, invert the tree, and return its root.

*Notes on Problem
* My implementation is a Post Order Traversal of the Tree
* The implementation uses recursion to find the leaf nodes, which then return the parent node to allow swapping
* Set the value of the left and right nodes to new TreeNode variables
* We switch the left and the right of the roots to ivnert the tree properly
* 
![image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/7b5327f3-bec2-45f7-bbdf-9a9c6b2041ad)






------------------------------------------------------------------------------------------------------------------------------------------------

EASY: [Problem 2]: Binary Search: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

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
EASY: [Problem 3]: Two sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

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

*Notes ON REVAMPED O(N) SOLUTION
* Optimized solution this time, O(n) instead of O(n^2)
* create a hashmap
* loop through array, constantly updating a variable equal to "target - nums[i]" after every iteration
* if the variable created is present in the hashmap
*     set the start index to the map.get(variable)
*     set the second index to the current index
*          break to reduce runtime
* Outside of the if, add the current value and its index to map
* (added at the end to avoid self reference)
 
------------------------------------------------------------------------------------------------------------------------------------------------
EASY: [Problem 4]: firstBadVersion: You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

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
EASY: [Problem 5]: Valid Parentheses: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

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
EASY: [Problem 6]: Best Stock Price: You are given an array prices where prices[i] is the price of a given stock on the ith day.

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
EASY: [Problem 7]: Valid Palindrome: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

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
EASY: [FIRST DYNAMIC PROGRAMMING PROBLEM: Problem 8]: Climbing Stairs: You are climbing a staircase. It takes n steps to reach the top.

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
EASY: [Problem 9]: Majority Element: Given an array nums of size n, return the majority element.

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
EASY: [Problem 10]: Contains Duplicate: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

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
EASY: [Problem 11]: Merge Two Sorted Lists: You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
[image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/69d23f55-2ff4-4bc4-8e60-850f10dfdc87)
*Notes
  * Return the head of the merged list, merged list in ascending order
  * So we need to make a dummy node that points to the first value
  * Create another ListNode 'current' that points to dummy
  * All we have to do is "rewire" the 'current' ListNode so it merges the lists in ascending order
  * While list1 is not null and list2 is not null
  *  Check which list's node is greater
  *    'Current' listNode then equals the list with the smaller node 
  *     list1/list2 = list1/list2.next
  *   Obviously have an else for list 1 and list 2 whichever one isn't greater
  *  outside of if/else, current = current.next
  *  outside of while loop:
  *  if list1/list 2 is not null, current.next = list1/list2. This is because after we went through the lists, one of them was outstandingly greater/smaller. so we just append what's left onto current
  * return dummy.next, since dummy is just the first value of current
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
EASY: FIRST PYTHON SOLUTION: [Problem 11]: Valid Anagram: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

*Notes
* All we need to do is check if the FREQUENCY of characters in the first string matches that of the second string
* We can do this by making 2 hashmaps (dictionaries in Python), one for string s and one for string t
* Then go through all characters in s. The 'key' is the character and the value is Hashmap.get(char, 0) +1
* Do the same for all characters in t.
* In python when we do equals equals for the two hashmaps, it will essentially check if the frequencies are the same.
* Function will return true if the frequencies in hashmaps are the same and false otherwise


  
------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
    
  EASY | FIRST DFS PROBLEM : [Problem 12]: Flood Fill: Given an m x n integer grid image where image[i][j] represents the pixel value of the image.
  
  You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

![image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/87527a8a-16e3-40b5-877f-406c5184fcf0)

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.


Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.


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
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
EASY: [Problem 13]: Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
![image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/80f7de00-48f1-404e-b5d7-d9fd5fafa90d)
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

![image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/68e55203-3d86-49f1-80ab-71871c337ea9)
Input: root = [4,2,7,1,3], val = 5
Output: []

*Notes
* First Binary Search Tree Problem, congratulations
* I felt like this was similar to a binary search.
* If the root value is bigger than the target, call the function again with it's left child which would be smaller
*  Likewise if the root value is smaller than the target, call the function again with it's right child which would be bigger
*  Return root if none of these are true
*  This should all be inside a if(root!= null), after that, return Null which means the target isn't available.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
FIRST MEDIUM: [Problem 14] : Lowest Common Ancestor of Binary Search Tree: Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


![image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/b7b087cc-03b5-42ad-a00b-28d25eebad84)
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

![image](https://github.com/syedshazli/Leetcode-Practice/assets/146783525/a4d976c2-807f-4529-86dc-bb142738e984)
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.



* This was very similar to the leetcode problem that searches for a target within a BST.
* All we really had to change was to say if the root is greater than p and q, search in the left (where all values of BST less than root are on left)
* if the root is less than p and q, search in the right(where all values of BST greater than root are on the right)
* else, return the root.
* This is a DFS implementation
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
EASY: [Problem 15]: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
#Notes
# I saw the remove and append method looking through W3 schools
# I saw that we can remove the current element if zero, and use append to send the zero to the end of the list
# Maintains order of the other elements!
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
