# Session : 23-10-24

## Question 1

Given a weighted, undirected, and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree. Also find the edges involved in formation of MST.

1. Expected Time Complexity: O($E log(V)$).
2. Expected Auxiliary Space: O($V²$).

* Example1:
V=5, edges = {(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (4, 2, 7)}
Result: 16 MST={(0, 1), (0, 3), (1, 2), (1, 4)}

## Question 2 

Given the root of a nearly complete binary tree, return the number of the nodes in the tree.

**NOTE: You have to make the tree from level order traversal.**

1. Time Complexity: O (log N* log N)
2. Space Complexity: O(H)

* Input:= [1,2,3,4,5,6] 
Output: 6

## Question 3 
Given a string `s`, find the longest palindromic subsequence's length in `s`. 
(A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.)

1. Time Complexity: O(NN)

* Input: s = "bbbab" 
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".