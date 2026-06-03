> 📌 **Cross-listed:** Primary location is [Array/0417-Pacific-Atlantic-Water-Flow](../../Array/0417-Pacific-Atlantic-Water-Flow). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**, **Matrix**

# 417. Pacific Atlantic Water Flow


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)


## 📝 Problem Description

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return *a **2D list** of grid coordinates *`result`* where *`result[i] = [r_i, c_i]`* denotes that rain water can flow from cell *`(r_i, c_i)`* to **both** the Pacific and Atlantic oceans*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)
```

**Input:** heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
**Output:** [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
**Explanation:** The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

```

Example 2:**

```

**Input:** heights = [[1]]
**Output:** [[0,0]]
**Explanation:** The water can flow from the only cell to the Pacific and Atlantic oceans.

```

 

**Constraints:**

	- `m == heights.length`

	- `n == heights[r].length`

	- `1 <= m, n <= 200`

	- `0 <= heights[r][c] <= 10^5`

## 🧠 Solution Explanation

## Intuition
The Pacific Atlantic Water Flow problem can be solved by identifying the cells that can flow to both the Pacific and Atlantic oceans. This approach works by simulating the flow of water from the edges of the oceans and finding the common cells that can be reached by both oceans. The key idea is to use a two-phase approach, where we first identify the cells that can flow to the Pacific ocean and then the cells that can flow to the Atlantic ocean.

## Approach
1. Initialize two queues, `pacific_nodes` and `atlantic_nodes`, to store the cells at the edges of the Pacific and Atlantic oceans, respectively.
2. Add the cells at the edges of the oceans to their respective queues and mark them as visited in the `pacific_seen` and `atlantic_seen` sets.
3. Define a helper function `check` to validate if a cell is within the grid boundaries and not visited before.
4. Define another helper function `get_coordinates` to perform a breadth-first search (BFS) from the cells in the queues and mark the reachable cells as visited.
5. Perform BFS from the Pacific and Atlantic oceans to find the cells that can flow to each ocean.
6. Find the intersection of the `pacific_seen` and `atlantic_seen` sets to get the cells that can flow to both oceans.

## Time Complexity
The time complexity is O(m*n), where m and n are the number of rows and columns in the grid, respectively. This is because in the worst case, we need to visit every cell in the grid.

## Space Complexity
The space complexity is O(m*n), where m and n are the number of rows and columns in the grid, respectively. This is because we need to store the visited cells in the `pacific_seen` and `atlantic_seen` sets.

## Key Insight
The key insight is to use a two-phase approach with BFS to simulate the flow of water from the edges of the oceans and find the common cells that can be reached by both oceans. This approach allows us to efficiently identify the cells that can flow to both the Pacific and Atlantic oceans.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 36 ms (Beats 32.91%) |
| 💾 Memory | 19.2 MB (Beats 100%) |
| 📅 Solved | 2025-10-06 |
| 💻 Language | Python |