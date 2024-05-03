# Leetcode-Practice
Join me on my leetcode journey.

Notes for specific problems:

Invert Binary Tree: Given the root of a binary tree, invert the tree, and return its root.

*Notes on Problem
* My implementation is a Post Order Traversal of the Tree
* The implementation uses recursion to find the leaf nodes, which then return the parent node to allow swapping
* We switch the left and the right of the roots to ivnert the tree properly






Binary Search: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

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

 
