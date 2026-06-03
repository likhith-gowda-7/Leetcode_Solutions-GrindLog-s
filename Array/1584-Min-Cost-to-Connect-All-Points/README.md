# 1584. Min Cost to Connect All Points


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Minimum Spanning Tree](https://img.shields.io/badge/Minimum%20Spanning%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/)


## 📝 Problem Description

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x_i, y_i]`.

The cost of connecting two points `[x_i, y_i]` and `[x_j, y_j]` is the **manhattan distance** between them: `|x_i - x_j| + |y_i - y_j|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)
```

**Input:** points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
**Output:** 20
**Explanation:** 
![](https://assets.leetcode.com/uploads/2020/08/26/c.png)
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

```

Example 2:**

```

**Input:** points = [[3,12],[-2,5],[-4,1]]
**Output:** 18

```

 

**Constraints:**

	- `1 <= points.length <= 1000`

	- `-10^6 <= x_i, y_i <= 10^6`

	- All pairs `(x_i, y_i)` are distinct.

## 🧠 Solution Explanation

**Intuition**
The problem is asking us to find the minimum cost to connect all points on a 2D-plane. The cost of connecting two points is the Manhattan distance between them. We can use Prim's algorithm to find the minimum spanning tree of the graph formed by these points, which will give us the minimum cost to connect all points.

**Approach**
1. Initialize a priority queue `heap` to store edges, where each edge is represented as a tuple `(cost, node)`.
2. Initialize a visited array `visited` to keep track of visited nodes, and a variable `total_edges` to count the number of edges in the minimum spanning tree.
3. Start with the first node (0) and add all its edges to the heap.
4. While the total number of edges is less than the number of nodes:
   1. Pop the edge with the minimum cost from the heap.
   2. If the node is already visited, skip it.
   3. Add the cost of the edge to the `MST_sum`.
   4. Mark the node as visited and increment the total number of edges.
   5. For each unvisited neighbor of the node, calculate the weight of the edge and add it to the heap.
5. Return the `MST_sum`, which is the minimum cost to connect all points.

**Time Complexity**
O(E log E) = O(E log V), where E is the number of edges and V is the number of vertices. This is because we use a priority queue to store edges, and each insertion and deletion operation takes O(log E) time.

**Space Complexity**
O(V + E), where V is the number of vertices and E is the number of edges. This is because we use a visited array to keep track of visited nodes, and a priority queue to store edges.

**Key Insight**
The key insight is to use Prim's algorithm to find the minimum spanning tree of the graph formed by the points. By starting with an arbitrary node and adding edges to the heap, we can efficiently find the minimum cost to connect all points. The priority queue ensures that we always consider the edge with the minimum cost, which leads to the optimal solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 619 ms (Beats 73.89%) |
| 💾 Memory | 82.5 MB (Beats 72.29%) |
| 📅 Solved | 2025-09-16 |
| 💻 Language | Python |