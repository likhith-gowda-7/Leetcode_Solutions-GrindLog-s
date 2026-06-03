> 📌 **Cross-listed:** Primary location is [Dynamic Programming/0787-Cheapest-Flights-Within-K-Stops](../../Dynamic-Programming/0787-Cheapest-Flights-Within-K-Stops). This problem also appears under: **Dynamic Programming**, **Depth-First Search**, **Breadth-First Search**, **Graph Theory**, **Heap (Priority Queue)**, **Shortest Path**

# 787. Cheapest Flights Within K Stops


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)


## 📝 Problem Description

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return ***the cheapest price** from *`src`* to *`dst`* with at most *`k`* stops. *If there is no such route, return* *`-1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)
```

**Input:** n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
**Output:** 700
**Explanation:**
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png)
```

**Input:** n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
**Output:** 200
**Explanation:**
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png)
```

**Input:** n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
**Output:** 500
**Explanation:**
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

```

 

**Constraints:**

	- `2 <= n <= 100`

	- `0 <= flights.length <= (n * (n - 1) / 2)`

	- `flights[i].length == 3`

	- `0 <= from_i, to_i < n`

	- `from_i != to_i`

	- `1 <= price_i <= 10^4`

	- There will not be any multiple flights between two cities.

	- `0 <= src, dst, k < n`

	- `src != dst`

## 🧠 Solution Explanation

**Intuition**
This solution uses a priority queue (implemented as a deque) to efficiently explore the graph and find the cheapest price from the source to the destination with at most k stops. The key insight is to maintain a costs array to keep track of the minimum cost to reach each node.

**Approach**
1. Create an adjacency list representation of the graph from the flights array.
2. Initialize a priority queue with the source node and a cost of 0, and a costs array with all elements set to infinity except for the source node which is set to 0.
3. While the priority queue is not empty, pop the node with the minimum cost and explore its neighbors.
4. For each neighbor, calculate the new cost by adding the edge cost to the current cost.
5. If the new cost is less than the current minimum cost to reach the neighbor, update the costs array and push the neighbor into the priority queue.
6. Repeat step 3-5 until the priority queue is empty.
7. Return the minimum cost to reach the destination node if it is not infinity, otherwise return -1.

**Time Complexity**
O(n * k * log(n)) where n is the number of nodes and k is the maximum number of stops. The priority queue operations (push and pop) take O(log(n)) time, and we perform these operations for each node and each possible number of stops.

**Space Complexity**
O(n + m) where n is the number of nodes and m is the number of edges. We need to store the adjacency list and the costs array.

**Key Insight**
The key insight is to use a priority queue to efficiently explore the graph and find the cheapest price with at most k stops. By maintaining a costs array, we can avoid recalculating the minimum cost to reach each node and improve the time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 88.4%) |
| 💾 Memory | 19.1 MB (Beats 100%) |
| 📅 Solved | 2025-09-06 |
| 💻 Language | Python |