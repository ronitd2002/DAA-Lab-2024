# Session : 07-08-2024

## Problem 1

Given two matrices A of size($m_1,n_1$) and B of size($m_2,n_2$). Find the multiplication of A & B if possible.

---

## Problem 2

Given an array `arr` of integer numbers, `arr[i]` represents the number of pages in the $i^{th}$ book. 

There are `m` number of students, and the task is to allocate all the books to the students. 

**Rules** :
* Each student gets at least one book
* Each book should be allocated to only 1 student
* Book allocation should be in **contiguous** manner.

Hence the condition should be that `len(arr) >= m` ALWAYS.

---

## Problem 3

Implement the Randomized QuickSort algorithm to sort a given array in ascending order. 

Guide: 
1. Random Pivot Selection: Select a pivot element randomly from the array.
2. Partitioning: Rearrange the array such that the elements less than the pivot are on its left, and the elements greater on its right.
3. Recursion: Recursively apply Randomized QuickSort to the subarrayson the left and right of the pivot. 

---

## Bonus:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. 
Optimize the TC and SC as much as you can.

Example: nums1 = [1,2], nums2 = [3,4]
Output: 2.500