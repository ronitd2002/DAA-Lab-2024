# Session : 24-08-2024

## Question 1

Sort an array of integers using the **Counting sort** algorithm.

## Question 2

Sort an array of integers using the **Bucket sort** algorithm.

## Question 3

You are given an integer array `arr` and an integer `k`, your task is to return the number of good subarrays in `arr`.

A 'good' subarray is defined as a contiguous part of the array that contains exactly k different integers. 

Example 1:
* **Input:** `arr` = [1,2,1,2,3], k= 2
* **Output:** 7
* **Explanation:** The subarrays with exactly 2 different integers are: [1,2], [2,1],[1,2], [2,3], [1,2,1], [2,1,2], and [1,2,1,2]

Example 2:
* **Input:** `arr` = [1,2,1,3,4], k= 3
* **Output:** 3
* **Explanation:** The subarrays with exactly 3 different integers are: [1,2,1,3], [2,1,3], [1,3,4]

Expected time complexity: O(N)
Aux space: O(k)