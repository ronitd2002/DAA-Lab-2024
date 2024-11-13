# Session : 06-11-2024

## Problem 1

Implement Bellman-Ford algorithm to an arbitrary graph.

## Problem 2

Implement Floyd-Warshall algorithm to an arbitrary graph.

## Problem 3

There are `n` cities numbered from 0 to $n-1$. Given the array edges where `edges[i]` = `[from, to, weight]` represents a bidirectional and weighted edge between cities from, and to, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distance Threshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Input: `n` = 4, `edges` = `[[0,1.3],[1,2,1],[1,3,4],[2,3,1]]`, `distanceThreshold` = 4

Output: 3