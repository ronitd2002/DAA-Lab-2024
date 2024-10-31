# Session : 30-10-2024

## Question 1

Write a program for a general undirected / directed graph demonstrating the **Dijkstra's shortest path algorithm** for graphs with non-negative edge weights

## Question 2

You are given an array prices where `prices[i]` is the price of a given stock on the ith day, and an integer fee representing a transaction fee. Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**NOTE**: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). The transaction fee is only charged once for each stock purchase and sale.

Example - 
Input: prices = `[1,3,2,8,4,9]`, Fee = 2 \
Output: 8 \
\
Expected Time Complexity - O($n^2$) \
Auxiliary Space Complexity - O($n^2$)

## Question 3

Mary is very, very happy. You would be happy, too, if your parents gave you the latest model BMW for your birthday. She wants to try out her new car, so she is going to visit her grandma. 

There is a graph with `N` vertices representing `N` cities and `M` edges representing bidirectional roads between some pairs of cities. We can assume that Mary lives in City 1 and her grandma lives in City `N`. Unfortunately, not everything is so good in life and examples are the speed limits. Mary decided to drive with permanent speed. Each of these `M` roads has a maximum permissible speed `V` that Mary can't exceed. Well, her whims don't end here. As a lover of extreme experiences, she wants to drive her expensive car as fast as possible.

You are to write a program to find the maximum speed at which Mary can reach her grandma's city without arguing with the policemen (for their own good).

* Example:
N = 4, M = 5
(u,v,weight) = `[[1,2,80],[4,3,300],[3,1,20],[2,4,90],[2,3,60]]`
Output: 80 \
\
*Use prim's algorithm using adjacency matrix due to time complexity constraints.*
