# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Shortest Path](https://img.shields.io/badge/Shortest%20Path-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)


## 📝 Problem Description

There are `n` cities numbered from `0` to `n-1`. Given the array `edges` where `edges[i] = [from_i, to_i, weight_i]` represents a bidirectional and weighted edge between cities `from_i` and `to_i`, and given the integer `distanceThreshold`.

Return the city with the smallest number of cities that are reachable through some path and whose distance is **at most** `distanceThreshold`, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities ***i*** and ***j*** is equal to the sum of the edges' weights along that path.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2024/08/23/problem1334example1.png)

```

**Input:** n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
**Output:** 3
**Explanation: **The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2024/08/23/problem1334example0.png)

```

**Input:** n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
**Output:** 0
**Explanation: **The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.

```

 

**Constraints:**

	- `2 <= n <= 100`

	- `1 <= edges.length <= n * (n - 1) / 2`

	- `edges[i].length == 3`

	- `0 <= from_i < to_i < n`

	- `1 <= weight_i, distanceThreshold <= 10^4`

	- All pairs `(from_i, to_i)` are distinct.

## 🧠 Solution Explanation

**Intuition**
The solution uses Dijkstra's algorithm to find the shortest distance from each city to all other cities. It then iterates through each city and counts the number of cities that are reachable within the given distance threshold. The city with the smallest count is returned.

**Approach**
1. Create an adjacency list representation of the graph from the given edges.
2. Initialize a distance matrix with infinite values, except for the diagonal which is 0 (since the distance from a city to itself is 0).
3. For each city, use Dijkstra's algorithm to find the shortest distance to all other cities. This is done by maintaining a priority queue of cities to visit, where the priority is the minimum distance from the current city to the visited city.
4. For each city, count the number of cities that are reachable within the given distance threshold.
5. Keep track of the city with the smallest count of reachable cities. If there are multiple such cities, keep track of the city with the greatest number.

**Time Complexity**
The time complexity of the solution is O(n^2 log n), where n is the number of cities. This is because for each city, we use Dijkstra's algorithm to find the shortest distance to all other cities, which takes O(n log n) time. We do this for n cities, resulting in a total time complexity of O(n^2 log n).

**Space Complexity**
The space complexity of the solution is O(n^2), where n is the number of cities. This is because we need to store the distance matrix, which has n^2 entries.

**Key Insight**
The key insight is to use Dijkstra's algorithm to find the shortest distance from each city to all other cities, and then iterate through each city to count the number of cities that are reachable within the given distance threshold. This approach allows us to efficiently find the city with the smallest number of neighbors at a threshold distance.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 187 ms (Beats 63.09%) |
| 💾 Memory | 19.1 MB (Beats 100%) |
| 📅 Solved | 2025-09-13 |
| 💻 Language | Python |